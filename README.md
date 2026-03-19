# Gemini Image Analyzer (Docker + PostgreSQL + Macvlan/Ipvlan)

This project implements a containerized web application for AI image analysis using **Google Gemini**, with **PostgreSQL** as the mandatory database.

It satisfies the assignment requirements for:
- Separate backend and database Dockerfiles
- Docker Compose orchestration
- Named volume persistence
- Static IP assignment on an external **macvlan/ipvlan** network
- Healthchecks and restart policies

## Stack

- Frontend: HTML + JavaScript served via Nginx
- Backend: FastAPI (Python)
- AI Model: Gemini (`google-generativeai`)
- Database: PostgreSQL (custom image via `database/Dockerfile`)
- Orchestration: Docker Compose
- Networking: macvlan OR ipvlan (external network)

## Project Structure

```text
.
├── backend/
│   ├── app/
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── gemini_service.py
│   │   ├── main.py
│   │   └── schemas.py
│   ├── .dockerignore
│   ├── Dockerfile
│   └── requirements.txt
├── database/
│   ├── init/01-bootstrap.sql
│   ├── .dockerignore
│   └── Dockerfile
├── frontend/
│   ├── .dockerignore
│   ├── Dockerfile
│   ├── index.html
│   └── nginx.conf
├── docker-compose.yml
├── .env.example
├── NETWORK_COMMANDS.md
└── REPORT.md
```

## 1) Configure Environment

Copy and edit environment variables:

```bash
cp .env.example .env
```

Set:
- `GEMINI_API_KEY` to your valid key
- `DOCKER_LAN_NETWORK` to your external network name
- `BACKEND_STATIC_IP`, `DB_STATIC_IP`, and `FRONTEND_STATIC_IP` to free LAN addresses in your subnet
- `FRONTEND_HOST_PORT` for same-host access
- PostgreSQL credentials

## 2) Create External Network (Mandatory)

Use one network mode from `NETWORK_COMMANDS.md`:
- macvlan (recommended for assignment demonstration)
- ipvlan (alternative)

## 3) Build and Run

```bash
docker compose up --build -d
```

Check containers:

```bash
docker compose ps
docker compose logs frontend frontend_local --tail=50
docker compose logs backend --tail=50
docker compose logs database --tail=50
```

## 4) Open Frontend

Use one of these options:

- LAN device access:

```bash
http://<FRONTEND_STATIC_IP>
```

- Same laptop/host access:

```bash
http://localhost:<FRONTEND_HOST_PORT>
```

Default host port in `.env` is `8088`.

The frontend calls `/api/*`, and Nginx proxies those requests to the backend container.

## API Endpoints

### Healthcheck

`GET /health`

Example:
```bash
curl http://<BACKEND_STATIC_IP>:8000/health
```

### Insert Record (Analyze + Store)

`POST /records`

Request body (URL image):
```json
{
  "image_url": "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05",
  "reference_text": "A landscape image likely showing nature."
}
```

Request body (base64 image):
```json
{
  "image_base64": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA...",
  "reference_text": "Check if this looks like a product photo."
}
```

Example command:
```bash
curl -X POST http://<BACKEND_STATIC_IP>:8000/records \
  -H "Content-Type: application/json" \
  -d "{\"image_url\":\"https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05\",\"reference_text\":\"Nature scene\"}"
```

### Fetch Records

`GET /records?limit=50`

Example:
```bash
curl http://<BACKEND_STATIC_IP>:8000/records?limit=10
```

## Persistence Verification

1. Insert one record via `POST /records`
2. Stop and remove containers:
   - `docker compose down`
3. Start again:
   - `docker compose up -d`
4. Call `GET /records`
5. Previously inserted records remain because of named volume `image_analyzer_postgres_data`

