import redis
import json

# Conexión a Redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def guardar_evento(evento, ttl=300):
    """
    Guarda un evento en Redis con un TTL (en segundos).
    """
    clave = f"evento:{evento['uuid']}"
    r.set(clave, json.dumps(evento), ex=ttl)

def obtener_evento(uuid):
    """
    Obtiene un evento desde Redis por su UUID.
    """
    clave = f"evento:{uuid}"
    valor = r.get(clave)
    return json.loads(valor) if valor else None

def listar_claves():
    """
    Lista todas las claves actuales en Redis.
    """
    return r.keys("evento:*")

def vaciar_cache():
    """
    Elimina todos los eventos del cache (solo los tipo evento:*).
    """
    claves = listar_claves()
    if claves:
        r.delete(*claves)
