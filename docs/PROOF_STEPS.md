# Screenshot Proof Steps

Use these commands and capture screenshots for your submission.

## 1) Network Inspect

```bash
docker network inspect image_analyzer_lan
```

## 1.1) Frontend Reachability

Open:

```bash
http://<FRONTEND_STATIC_IP>
```

Take a screenshot of the UI loading in browser.

## 2) Container IPs

```bash
docker inspect -f "{{.Name}} -> {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}" image-analyzer-api image-analyzer-db
```

Or with frontend:

```bash
docker inspect -f "{{.Name}} -> {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}" image-analyzer-frontend image-analyzer-api image-analyzer-db
```

## 3) Volume Persistence

```bash
curl -X POST http://<BACKEND_STATIC_IP>:8000/records \
  -H "Content-Type: application/json" \
  -d "{\"image_url\":\"https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05\",\"reference_text\":\"nature\"}"

docker compose down
docker compose up -d

curl http://<BACKEND_STATIC_IP>:8000/records?limit=10
```

Take screenshots:
- POST success response
- `docker compose down` and `up -d`
- GET response still showing inserted record
