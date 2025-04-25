# Tarea1SD: Plataforma de Análisis de Tráfico Región Metropolitana 🚦

Proyecto de Sistemas Distribuidos - 2025-1

## 📚 Descripción

Este proyecto tiene como objetivo desarrollar una plataforma distribuida capaz de **extraer, almacenar, cachear y consultar eventos de tráfico** en tiempo real de la Región Metropolitana de Chile utilizando datos del **Live Map de Waze**.

La plataforma implementa:

- **Scraper**: para extraer eventos viales.
- **Almacenamiento**: en base de datos **PostgreSQL**.
- **Caché**: de eventos recientes en **Redis**.
- **API REST**: desarrollada en **FastAPI** para consultar los eventos.

Todo el sistema está diseñado en forma modular y desplegado usando **Docker Compose**.

---

## 📂 Estructura del Proyecto

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.11**
- **FastAPI** (API REST)
- **PostgreSQL 15** (Base de datos)
- **Redis 7** (Sistema de caché)
- **Docker y Docker Compose**
- **Requests** (para web scraping)

---

## ⚙️ Instalación y Ejecución

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Jairo-Ch/Tarea1SD.git
   cd Tarea1SD
   
2. Levanta los servicios con Docker Compose:
    ```bash
    docker compose up --build



    Esto levantará automáticamente:

PostgreSQL (Base de datos)

Redis (Sistema de cache)

traffic_api (API REST construida con FastAPI)


       
Esto levantará automáticamente:

Base de datos PostgreSQL

Redis

FastAPI en http://localhost:8000

(Opcional) Activa el entorno virtual si deseas correr scripts:

bash
Copiar
source venv/bin/activate
(Opcional) Ejecuta scripts manualmente:

Insertar eventos a PostgreSQL:

bash
Copiar
python3 storage/insertar_eventos.py
Cargar eventos recientes a Redis:

bash
Copiar
python3 storage/carga_a_redis.py
Accede a la documentación interactiva en Swagger UI:

bash
Copiar
http://localhost:8000/docs
🌐 Endpoints Disponibles
GET /eventos/recientes

Devuelve los eventos más recientes desde Redis.

GET /eventos/zona?ciudad={nombre}

Consulta eventos de una ciudad específica desde PostgreSQL.

GET /eventos/tipo?tipo={tipo}

Consulta eventos filtrados por tipo desde PostgreSQL.

📊 Resultados de Pruebas de Rendimiento
Se midieron los tiempos de respuesta promedio de los endpoints:


Endpoint	Tiempo Promedio
/eventos/recientes	0.0041 segundos
/eventos/zona?ciudad=...	0.0159 segundos
/eventos/tipo?tipo=...	0.0435 segundos
Pruebas ejecutadas con el script tests/pruebas_rendimiento.py.

📦 Consideraciones Finales
Eventos extraídos: Más de 10.000 eventos únicos recopilados desde Waze Live Map.

Distribución de servicios: Cada servicio corre en un contenedor Docker independiente.

Alta disponibilidad: Redis y PostgreSQL permiten respuestas rápidas y fiables.

Modularidad: La arquitectura está lista para escalar e integrar nuevas funcionalidades.

🚀 Flujo de Pruebas Rápido
Levanta los servicios:

bash
Copiar
docker compose up --build
Inserta eventos si es necesario:

bash
Copiar
python3 storage/insertar_eventos.py
Carga eventos recientes a Redis:

bash
Copiar
python3 storage/carga_a_redis.py
Haz pruebas de rendimiento:

bash
Copiar
python3 tests/pruebas_rendimiento.py
📎 Repositorio
🔗 Repositorio GitHub - Tarea1SD

