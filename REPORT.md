# Assignment Report: Containerized AI Image Analyzer

## 1. Project Overview

This project delivers a production-oriented containerized web application that analyzes images using the Gemini API and stores the analysis output in PostgreSQL.

### Core Goals Achieved

- Frontend web UI integrated through an Nginx container
- PostgreSQL used as the mandatory database
- Backend API implemented with FastAPI
- Separate Dockerfiles for backend and database
- Docker Compose orchestration for the full stack
- External macvlan/ipvlan network integration with static IP addresses
- Persistent storage through a named Docker volume
- Healthcheck, restart policy, and service dependency handling

The backend exposes:
- `POST /records` to analyze image content and insert a record
- `GET /records` to fetch stored records
- `GET /health` to verify backend and database status

## 2. Architecture and Flow

### 2.1 Logical Flow

1. Client opens the frontend web UI running in a dedicated container.
2. Frontend sends API calls to `/api/*`, proxied by Nginx to the backend container.
3. Backend validates input and obtains image bytes.
4. Backend calls Gemini model for image interpretation and reference comparison.
5. Backend inserts structured analysis into PostgreSQL.
6. Frontend renders API responses and recent records to the user.

### 2.2 Network Design Diagram

```text
   +-------------------------+
   | Client (Browser)        |
   +-----------+-------------+
               |
               | HTTP (LAN)
               v
   +-----------------------------+
   | Frontend Container          |
   | image-analyzer-frontend     |
   | Static IP: FRONTEND_STATIC_IP|
   +--------------+--------------+
                  |
                  | HTTP /api/*
                  v
   +-----------------------------+
   | Backend Container           |
   | image-analyzer-api          |
   | Static IP: BACKEND_STATIC_IP|
   +--------------+--------------+
                  |
                  | TCP 5432
                  v
   +-----------------------------+
   | PostgreSQL Container        |
   | image-analyzer-db           |
   | Static IP: DB_STATIC_IP     |
   +--------------+--------------+
                  |
                  v
      Named Volume: image_analyzer_postgres_data

External Docker Network: macvlan OR ipvlan
```

## 3. Container Build Optimization

### 3.1 Backend Image Optimization

The backend Dockerfile uses a **multi-stage build**:

- **Builder stage**
  - Creates virtual environment
  - Installs Python dependencies once
  - Uses `--no-cache-dir` to reduce layer bloat
- **Runtime stage**
  - Copies only virtual environment + app code
  - Excludes pip cache and build artifacts
  - Runs with a dedicated non-root user (`appuser`)

This approach reduces image size and attack surface compared with single-stage builds.

### 3.2 Minimal Base Images

- Backend: `python:3.12-slim`
- Database: `postgres:16-alpine`

Both are smaller than full distro images and better suited for production.

### 3.3 Layer and Context Hygiene

`.dockerignore` is provided in both backend and database folders to avoid copying:
- caches
- logs
- editor metadata
- temporary artifacts

This improves build speed and avoids unnecessary layers.

## 4. Image Size Comparison

### 4.1 Measurement Commands

Run the following after build:

```bash
docker compose build --no-cache
docker images | grep -E "image-analyzer|REPOSITORY"
```

### 4.2 Comparison Table Template

Use the measured output to populate:

| Component | Unoptimized (single stage/full base) | Optimized (current) | Gain |
|---|---:|---:|---:|
| Backend | (measure) | (measure) | (calculate) |
| Database | (measure) | (measure) | (calculate) |

Expected trend:
- backend optimized image should be significantly smaller than a naive single-stage image
- database image remains compact with alpine base and limited customization

## 5. Networking Design (Macvlan/Ipvlan)

### 5.1 Why External L2 Network

The assignment requires LAN-reachable containers with static IP addresses.  
An external `macvlan` or `ipvlan` network supports direct Layer-2 style addressing on the LAN subnet.

### 5.2 Static IP Assignment

Static IPs are assigned in `docker-compose.yml`:
- backend: `${BACKEND_STATIC_IP}`
- database: `${DB_STATIC_IP}`

This ensures predictable addressing for API access and DB connectivity.

### 5.3 Subnet and Gateway

Subnet and gateway are configured during manual network creation:
- `--subnet=...`
- `--gateway=...`
- `-o parent=...`

### 5.4 Host Isolation in Macvlan

In macvlan mode, host-to-container communication is often blocked by design.
- Containers can usually talk to LAN peers.
- Host may require a separate macvlan interface and routing rules to reach containers directly.

This is a known behavior and must be documented for deployment planning.

## 6. Macvlan vs Ipvlan Comparison

| Criteria | Macvlan | Ipvlan |
|---|---|---|
| Container identity on LAN | Unique MAC per container | Shares parent MAC behavior |
| Switch/infra compatibility | Can stress MAC tables at scale | Better MAC scalability |
| Host-container communication | Often isolated by default | Usually easier depending on mode |
| Typical use | Direct L2 presence per container | Lower-overhead L2/L3 variants |
| Assignment fit | Excellent for demonstrating LAN presence | Also valid and often more scalable |

Conclusion:
- For demonstration clarity, macvlan is intuitive.
- For larger deployments, ipvlan may be operationally cleaner.

## 7. Persistence and Reliability Validation

### 7.1 Named Volume Persistence

Database data lives in:
- `image_analyzer_postgres_data` named volume

Validation sequence:
1. Insert record using `POST /records`
2. Run `docker compose down`
3. Run `docker compose up -d`
4. Fetch with `GET /records`
5. Record still exists

### 7.2 Healthchecks and Restart

- Database healthcheck: `pg_isready`
- Backend healthcheck: internal HTTP call to `/health`
- Frontend healthcheck: internal HTTP check on Nginx root path
- Restart policy: `unless-stopped`
- Startup ordering: `depends_on` with `condition: service_healthy`

These controls improve service reliability and startup correctness.

## 8. Screenshot Evidence Checklist

Capture and include screenshots for:

1. Network inspection output:
   - `docker network inspect <network-name>`
2. Container IP addresses:
   - `docker inspect -f "{{.Name}} -> {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}" image-analyzer-api image-analyzer-db`
3. Volume persistence test:
   - `POST /records` success
   - `docker compose down && docker compose up -d`
   - `GET /records` still returns inserted data
4. Running containers:
   - `docker compose ps`

## 9. Conclusion

The delivered solution satisfies assignment constraints and demonstrates practical production concerns:
- container image optimization
- secure environment-based configuration
- service orchestration
- persistent storage
- external LAN networking with static addressing

