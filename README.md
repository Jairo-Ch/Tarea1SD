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

Tarea1SD/ ├── docker-compose.yml ├── README.md ├── requirements.txt ├── event_collector/ │ └── eventos.json │ └── waze_scraper_masivo.py ├── storage/ │ └── crear_tabla.py │ └── insertar_eventos.py │ └── carga_a_redis.py │ └── cache_manager.py ├── traffic_api/ │ └── Dockerfile │ └── main.py ├── tests/ │ └── pruebas_rendimiento.py └── venv/

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
   ```

2. Levanta los servicios con Docker Compose:
   ```bash
   docker compose up --build
   ```

Esto levantará automáticamente:

- **PostgreSQL** (Base de datos)
- **Redis** (Sistema de caché)
- **traffic_api** (API REST construida con FastAPI disponible en `http://localhost:8000`)

---

(Opcional) Activa el entorno virtual si deseas correr scripts manualmente:
```bash
source venv/bin/activate
```

(Opcional) Ejecuta scripts manualmente:

- Insertar eventos a PostgreSQL:
  ```bash
  python3 storage/insertar_eventos.py
  ```

- Cargar eventos recientes a Redis:
  ```bash
  python3 storage/carga_a_redis.py
  ```

---

Accede a la documentación interactiva Swagger UI:

```
http://localhost:8000/docs
```

---

## 🌐 Endpoints Disponibles

- **GET /eventos/recientes**  
  Devuelve los eventos más recientes desde Redis.

- **GET /eventos/zona?ciudad={nombre}**  
  Consulta eventos de una ciudad específica desde PostgreSQL.

- **GET /eventos/tipo?tipo={tipo}**  
  Consulta eventos filtrados por tipo desde PostgreSQL.

---

## 📊 Resultados de Pruebas de Rendimiento

Se midieron los tiempos de respuesta promedio de los endpoints:

| Endpoint                     | Tiempo Promedio    |
|-------------------------------|--------------------|
| `/eventos/recientes`          | 0.0041 segundos    |
| `/eventos/zona?ciudad=...`    | 0.0159 segundos    |
| `/eventos/tipo?tipo=...`      | 0.0435 segundos    |

> Las pruebas fueron ejecutadas utilizando el script `tests/pruebas_rendimiento.py`.
