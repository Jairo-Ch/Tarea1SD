# traffic_generator/generador_uniforme.py

import requests
import random
import time

# Configuración
ENDPOINTS = [
    "http://localhost:8000/eventos/recientes",
    "http://localhost:8000/eventos/zona?ciudad=Pudahuel",
    "http://localhost:8000/eventos/tipo?tipo=HAZARD"
]

# Intervalo de tiempo entre consultas (segundos)
INTERVALO_MIN = 0.5
INTERVALO_MAX = 2.0

# Cantidad de consultas que queremos hacer
TOTAL_CONSULTAS = 100

print("🚀 Iniciando generador de tráfico uniforme...")

for i in range(TOTAL_CONSULTAS):
    endpoint = random.choice(ENDPOINTS)
    try:
        inicio = time.time()
        response = requests.get(endpoint, timeout=5)
        duracion = time.time() - inicio
        print(f"✅ [{i+1}/{TOTAL_CONSULTAS}] {endpoint} | Código: {response.status_code} | Tiempo: {duracion:.4f}s")
    except Exception as e:
        print(f"❌ Error en la consulta: {e}")

    # Espera un tiempo aleatorio uniforme entre INTERVALO_MIN y INTERVALO_MAX
    time.sleep(random.uniform(INTERVALO_MIN, INTERVALO_MAX))

print("🏁 Generador de tráfico uniforme finalizado.")
