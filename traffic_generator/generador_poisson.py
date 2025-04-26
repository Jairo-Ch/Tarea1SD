import requests
import time
import random

# 📚 Configuración
TOTAL_CONSULTAS = 100
LAMBDA = 0.5  # tasa de llegada promedio (eventos por segundo)

# Endpoints disponibles
ENDPOINTS = [
    "http://localhost:8000/eventos/recientes",
    "http://localhost:8000/eventos/zona?ciudad=Pudahuel",
    "http://localhost:8000/eventos/tipo?tipo=HAZARD",
]

print("🚀 Iniciando generador de tráfico Poisson...")

for i in range(1, TOTAL_CONSULTAS + 1):
    url = random.choice(ENDPOINTS)
    try:
        inicio = time.time()
        response = requests.get(url, timeout=5)
        fin = time.time()
        print(f"✅ [{i}/{TOTAL_CONSULTAS}] {url} | Código: {response.status_code} | Tiempo: {fin - inicio:.4f}s")
    except Exception as e:
        print(f"❌ Error en la consulta {url}: {e}")
    
    # ⏳ Espera un tiempo aleatorio antes de la siguiente consulta
    espera = random.expovariate(LAMBDA)
    time.sleep(espera)
print("🏁 Generador de tráfico Poisson finalizado.")
