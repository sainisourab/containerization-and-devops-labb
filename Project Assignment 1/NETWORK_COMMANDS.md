# External Network Creation Commands

Choose **one** mode for the assignment (macvlan or ipvlan).  
Replace placeholders before running.

## Option A: Macvlan

```bash
docker network create -d macvlan \
  --subnet=192.168.1.0/24 \
  --gateway=192.168.1.1 \
  -o parent=eth0 \
  image_analyzer_lan
```

Windows Docker Desktop users may use a different parent interface (for example `Ethernet` or a WSL bridge), depending on your host setup.

## Option B: Ipvlan

```bash
docker network create -d ipvlan \
  --subnet=192.168.1.0/24 \
  --gateway=192.168.1.1 \
  -o parent=eth0 \
  image_analyzer_lan
```

## Validate Network

```bash
docker network inspect image_analyzer_lan
```

## Validate Container IP Assignment

```bash
docker inspect -f "{{.Name}} -> {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}" image-analyzer-api image-analyzer-db
```

Or include frontend as well:

```bash
docker inspect -f "{{.Name}} -> {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}" image-analyzer-frontend image-analyzer-api image-analyzer-db
```

## Validate LAN Reachability

From another machine in the same LAN:

```bash
curl http://<BACKEND_STATIC_IP>:8000/health
```

## Macvlan Host Isolation Note

In macvlan mode, the host usually cannot directly communicate with macvlan containers unless a host-side macvlan interface is created and routed explicitly.
