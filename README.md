Tarea1SD: Plataforma de Análisis de Tráfico Región Metropolitana 🚦
Proyecto de Sistemas Distribuidos - 2025-1

📚 Descripción
Este proyecto tiene como objetivo desarrollar una plataforma distribuida capaz de extraer, almacenar, cachear y consultar eventos de tráfico en tiempo real de la Región Metropolitana de Chile utilizando datos del Live Map de Waze.

La plataforma implementa:

Scraper: para extraer eventos viales.

Almacenamiento: en base de datos PostgreSQL.

Caché: de eventos recientes en Redis.

API REST: desarrollada en FastAPI para consultar los eventos.

Todo el sistema está diseñado en forma modular y desplegado usando Docker Compose.

📂 Estructura del Proyecto
pgsql
Copiar
Tarea1SD/
├── docker-compose.yml
├── README.md
├── event_collector/
│   └── waze_scraper_masivo.py
│   └── eventos.json
├── storage/
│   └── crear_tabla.py
│   └── insertar_eventos.py
│   └── carga_a_redis.py
│   └── cache_manager.py
├── traffic_api/
│   └── main.py
│   └── Dockerfile
├── tests/
│   └── pruebas_rendimiento.py
└── requirements.txt
🛠️ Tecnologías Utilizadas
Python 3.11

FastAPI (API REST)

PostgreSQL 15 (Base de datos)

Redis 7 (Sistema de caché)

Docker y Docker Compose

Requests (para web scraping)

⚙️ Instalación y Ejecución
Clona el repositorio:

bash
Copiar
git clone https://github.com/Jairo-Ch/Tarea1SD.git
cd Tarea1SD
Levanta todos los servicios con Docker:

bash
Copiar
docker compose up --build
Activa el entorno virtual (opcional si deseas ejecutar scripts locales):

bash
Copiar
source venv/bin/activate
Abre en tu navegador:

bash
Copiar
http://localhost:8000/docs
para explorar la API creada con FastAPI.

📈 Endpoints Disponibles
GET /eventos/recientes
Devuelve los eventos más recientes almacenados en Redis.

GET /eventos/zona?ciudad={nombre}
Devuelve eventos almacenados en PostgreSQL filtrados por ciudad.

GET /eventos/tipo?tipo={tipo}
Devuelve eventos almacenados en PostgreSQL filtrados por tipo de evento.

📊 Pruebas de Rendimiento
Se realizaron pruebas de rendimiento simulando consultas concurrentes:


Endpoint	Tiempo Promedio de Respuesta
/eventos/recientes	0.0041 segundos
/eventos/zona	0.0159 segundos
/eventos/tipo	0.0435 segundos
📝 Notas Finales
Se recolectaron más de 10.000 eventos únicos desde Waze.

Se utilizó un enfoque modular para facilitar el mantenimiento y escalabilidad.

El diseño permite extender el proyecto a otras regiones fácilmente.

📌 Repositorio
GitHub - Tarea1SD
