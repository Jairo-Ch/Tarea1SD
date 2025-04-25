from fastapi import FastAPI, Query
import redis
import json
import psycopg2

# 💡 Aquí defines el objeto `app` antes de usarlo
app = FastAPI()

# Redis
r = redis.Redis(host="localhost", port=6379, decode_responses=True)

@app.get("/eventos/recientes")
def eventos_recientes():
    claves = r.keys("evento:*")
    eventos = [json.loads(r.get(k)) for k in claves if r.get(k)]
    return {"total": len(eventos), "eventos": eventos}

# PostgreSQL
def obtener_conexion_postgres():
    return psycopg2.connect(
        dbname="trafico",
        user="jairo",
        password="1234",
        host="localhost"
    )

@app.get("/eventos/zona")
def eventos_por_ciudad(ciudad: str = Query(...)):
    conn = obtener_conexion_postgres()
    cur = conn.cursor()
    cur.execute("""
        SELECT uuid, tipo, subtipo, ciudad, calle, lat, lon, usuario, fecha
        FROM eventos
        WHERE ciudad ILIKE %s
    """, (f"%{ciudad}%",))
    columnas = [desc[0] for desc in cur.description]
    eventos = [dict(zip(columnas, fila)) for fila in cur.fetchall()]
    cur.close()
    conn.close()
    return {"ciudad": ciudad, "total": len(eventos), "eventos": eventos}

@app.get("/eventos/tipo")
def eventos_por_tipo(tipo: str = Query(..., description="Tipo de evento: ACCIDENT, JAM, POLICE, HAZARD, ROAD_CLOSED, etc.")):
    conn = obtener_conexion_postgres()
    cur = conn.cursor()
    cur.execute("""
        SELECT uuid, tipo, subtipo, ciudad, calle, lat, lon, usuario, fecha
        FROM eventos
        WHERE tipo ILIKE %s
    """, (f"%{tipo}%",))
    columnas = [desc[0] for desc in cur.description]
    eventos = [dict(zip(columnas, fila)) for fila in cur.fetchall()]
    cur.close()
    conn.close()

    return {"tipo": tipo, "total": len(eventos), "eventos": eventos}
