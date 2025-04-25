import requests
import json
import time
import os
import random

# Región Metropolitana
LAT_MIN = -33.75
LAT_MAX = -33.30
LON_MIN = -70.85
LON_MAX = -70.45

# Configuración
RADIO = 0.02
MAX_EVENTOS = 10000
eventos = {}
nuevos_este_rango = 0
total_consultas = 0

URL_TEMPLATE = "https://www.waze.com/live-map/api/georss?top={top}&bottom={bottom}&left={left}&right={right}&env=row&types=alerts,traffic"

# ✅ Cargar eventos anteriores
if os.path.exists("eventos.json"):
    with open("eventos.json", "r", encoding="utf-8") as f:
        prev = json.load(f)
        eventos = {e["uuid"]: e for e in prev}
    print(f"🔁 Se cargaron {len(eventos)} eventos desde 'eventos.json'")

# 🔄 Realizar consultas dinámicas
while len(eventos) < MAX_EVENTOS:
    centro_lat = random.uniform(LAT_MIN, LAT_MAX)
    centro_lon = random.uniform(LON_MIN, LON_MAX)

    top = centro_lat
    bottom = centro_lat - RADIO
    left = centro_lon
    right = centro_lon + RADIO

    url = URL_TEMPLATE.format(top=top, bottom=bottom, left=left, right=right)
    print(f"🌍 Consultando: {top:.3f}, {left:.3f} -> {bottom:.3f}, {right:.3f}")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        for alerta in data.get("alerts", []):
            uuid = alerta.get("uuid")
            if uuid and uuid not in eventos:
                eventos[uuid] = {
                    "tipo": alerta.get("type"),
                    "subtipo": alerta.get("subtype"),
                    "ciudad": alerta.get("city"),
                    "calle": alerta.get("street"),
                    "lat": alerta.get("location", {}).get("y"),
                    "lon": alerta.get("location", {}).get("x"),
                    "usuario": alerta.get("reportBy"),
                    "fecha": alerta.get("pubMillis"),
                    "uuid": uuid
                }
                nuevos_este_rango += 1
                print(f"🆕 {alerta.get('type')} en {alerta.get('city')} - {alerta.get('street')}")
                print(f"📈 Total eventos hasta ahora: {len(eventos)}")

    except requests.exceptions.Timeout:
        print("⏳ Timeout al consultar:", url)
    except requests.exceptions.RequestException as e:
        print("❌ Error en la consulta:", e)
    except Exception as e:
        print("⚠️ Otro error inesperado:", e)

    total_consultas += 1
    time.sleep(0.2)  # ⚠️ Mantener para evitar bloqueo del servidor

# 💾 Guardar
with open("eventos.json", "w", encoding="utf-8") as f:
    json.dump(list(eventos.values()), f, indent=2, ensure_ascii=False)

print(f"\n✅ Se realizaron {total_consultas} consultas aleatorias")
print(f"🆕 Eventos nuevos en esta ejecución: {nuevos_este_rango}")
print(f"📦 Total acumulado: {len(eventos)} eventos únicos")
print("📁 Archivo 'eventos.json' actualizado ✅")
