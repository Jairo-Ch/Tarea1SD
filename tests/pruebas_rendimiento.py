import time
import requests

BASE_URL = "http://localhost:8000"

def medir_tiempo(endpoint, params=None):
    inicio = time.time()
    r = requests.get(f"{BASE_URL}{endpoint}", params=params)
    duracion = time.time() - inicio
    return duracion, r.status_code

def prueba_eventos_recientes(n=10):
    print("📦 Probando /eventos/recientes (Redis)")
    tiempos = []
    for _ in range(n):
        dur, status = medir_tiempo("/eventos/recientes")
        tiempos.append(dur)
    print(f"⏱️ Promedio: {sum(tiempos)/n:.4f}s\n")

def prueba_eventos_zona(ciudad="Pudahuel", n=10):
    print(f"🏙️ Probando /eventos/zona?ciudad={ciudad} (PostgreSQL)")
    tiempos = []
    for _ in range(n):
        dur, status = medir_tiempo("/eventos/zona", {"ciudad": ciudad})
        tiempos.append(dur)
    print(f"⏱️ Promedio: {sum(tiempos)/n:.4f}s\n")

def prueba_eventos_tipo(tipo="ROAD_CLOSED", n=10):
    print(f"🚧 Probando /eventos/tipo?tipo={tipo} (PostgreSQL)")
    tiempos = []
    for _ in range(n):
        dur, status = medir_tiempo("/eventos/tipo", {"tipo": tipo})
        tiempos.append(dur)
    print(f"⏱️ Promedio: {sum(tiempos)/n:.4f}s\n")

if __name__ == "__main__":
    prueba_eventos_recientes()
    prueba_eventos_zona("Pudahuel")
    prueba_eventos_tipo("HAZARD")
