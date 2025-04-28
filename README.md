# Tarea1SD: Plataforma de Análisis de Tráfico Región Metropolitana

Proyecto de Sistemas Distribuidos - 2025-1

---

## Descripción

Este proyecto desarrolla una plataforma distribuida capaz de **extraer, almacenar, cachear y consultar eventos de tráfico** en tiempo real para la Región Metropolitana de Chile, utilizando datos públicos del **Live Map de Waze**.

La plataforma incluye:

- **Scraper** para extraer eventos de tráfico.
- **Almacenamiento** en base de datos **PostgreSQL**.
- **Sistema de caché** de eventos recientes usando **Redis**.
- **API REST** desarrollada en **FastAPI** para consultar eventos.
- **Generadores de tráfico sintético** para pruebas de carga.

Todo el sistema está construido de forma modular y desplegado con **Docker Compose**.

---

## Estructura del Proyecto


```
Tarea1SD/
├── docker-compose.yml
├── README.md
├── event_collector/
│   ├── contar_eventos.py
│   ├── eventos.json
│   └── waze_scraper_masivo.py
├── storage/
│   ├── cache_manager.py
│   ├── carga_a_redis.py
│   ├── crear_tabla.py
│   ├── insertar_eventos.py
│   ├── probar_cache.py
│   └── probar_redis.py
├── tests/
│   └── pruebas_rendimiento.py
├── traffic_api/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── traffic_generator/
│   ├── generador_poisson.py
│   └── generador_uniforme.py
└── venv/ (entorno virtual)
```





---

## Tecnologías Utilizadas

- **Python 3.11**
- **FastAPI** (Framework para APIs REST)
- **PostgreSQL 15** (Base de datos relacional)
- **Redis 7** (Sistema de almacenamiento en memoria)
- **Docker** y **Docker Compose**
- **Requests** (para consultas HTTP)
- **Psycopg2** (conexión a PostgreSQL)

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
- Contar eventos en eventos.json::
  ```bash
  python3 event_collector/contar_eventos.py
  ```
- Ejecutar generadores de tráfico:
  ```bash
  python3 traffic_generator/generador_poisson.py
  python3 traffic_generator/generador_uniforme.py
  ```
  

---

Accede a la documentación interactiva Swagger UI:

FastAPI genera automáticamente una documentación interactiva accesible en:
```
http://localhost:8000/docs
```
Permite explorar los endpoints, probar consultas y visualizar resultados directamente desde el navegador.
---

##  Endpoints Disponibles

- **GET /eventos/recientes**  
  Devuelve los eventos más recientes desde Redis.

- **GET /eventos/zona?ciudad={nombre}**  
  Consulta eventos de una ciudad específica desde PostgreSQL.

- **GET /eventos/tipo?tipo={tipo}**  
  Consulta eventos filtrados por tipo desde PostgreSQL.

---

## Resultados de Pruebas de Rendimiento

Se midieron los tiempos de respuesta promedio de los endpoints usando 
tests/pruebas_rendimiento.py:

| Endpoint                      | Tiempo Promedio    |
|-------------------------------|--------------------|
| `/eventos/recientes`(Redis)   | 0.0049  segundos   |
| `/eventos/zona?ciudad=...`    | 0.0153 segundos    |
| `/eventos/tipo?tipo=...`      | 0.0447 segundos    |

## Organización de Scripts Manuales

- **event_collector:** Contiene el scraper que descarga eventos de tráfico desde Waze.
- **storage:** Scripts para gestionar la base de datos PostgreSQL y el caché Redis.
- **traffic_generator:** Scripts que generan tráfico sintético para pruebas de carga.
- **traffic_api:** Servicio FastAPI que expone la API REST para consultar eventos.
- **tests:** Scripts para realizar pruebas de rendimiento del sistema.


## Notas Finales


Este proyecto demuestra el uso de arquitecturas modulares, caché inteligente y diseño de APIs RESTful, aplicados a un sistema de datos urbanos en tiempo real.
