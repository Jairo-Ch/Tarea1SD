import json
import psycopg2

# Conexión a PostgreSQL
conn = psycopg2.connect(
    dbname="trafico",
    user="jairo",
    password="1234",
    host="localhost"
)
cur = conn.cursor()

# Cargar eventos desde JSON
with open("../event_collector/eventos.json", "r", encoding="utf-8") as f:
    eventos = json.load(f)

insertados = 0
for evento in eventos:
    try:
        cur.execute("""
            INSERT INTO eventos (uuid, tipo, subtipo, ciudad, calle, lat, lon, usuario, fecha)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (uuid) DO NOTHING
        """, (
            evento.get("uuid"),
            evento.get("tipo"),
            evento.get("subtipo"),
            evento.get("ciudad"),
            evento.get("calle"),
            evento.get("lat"),
            evento.get("lon"),
            evento.get("usuario"),
            evento.get("fecha")
        ))
        insertados += 1
    except Exception as e:
        print("❌ Error al insertar:", e)
        conn.rollback()

conn.commit()
cur.close()
conn.close()

print(f"✅ Se insertaron {insertados} eventos nuevos.")
