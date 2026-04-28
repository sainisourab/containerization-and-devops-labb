

<div style='page-break-after: always;'></div>



## **Containerization and DevOps Lab**
## **EXPERIMENT – 01**

**Aim of the Experiment**

To study, install, configure, and compare Virtual Machines and Containers using VirtualBox, Vagrant, Docker, and WSL on a Windows system.

**Objective**

- To understand the conceptual and practical differences between Virtual Machines and Containers.
- To install and configure a Virtual Machine using VirtualBox and Vagrant on Windows.
- To install and configure Containers using Docker inside WSL.
- To deploy an Ubuntu-based Nginx web server in both environments.
- To compare resource utilization, performance, and operational characteristics of VMs and Containers.

**System Configuration / Requirements**
System Configuration
- Operating System: Windows 11
- Processor: Intel/AMD x64 Processor
- RAM: 8 GB
- Storage: Minimum 20 GB free space

Software Requirements
- Oracle VirtualBox
- Vagrant
- Docker Engine
- Windows Subsystem for Linux (WSL 2)
- Ubuntu (WSL)

**Theory**

**Virtual Machine (VM)**

A Virtual Machine emulates a complete physical computer, including its own operating system kernel, hardware drivers, and user space. Each VM runs on top of a hypervisor.

**Characteristics:**

- Full OS per VM
- Higher resource usage
- Strong isolation
- Slower startup time


**Container**

Containers virtualize at the operating system level. They share the host OS kernel while isolating applications and dependencies in user space.

**Characteristics:**

- Shared kernel
- Lightweight
- Fast startup
- Efficient resource usage

**Advantages and Disadvantages**

**Advantages of Virtual Machines**

- Provides **strong isolation** since each VM runs its own operating system.
- Supports **multiple operating systems** on the same host machine.
- Suitable for **legacy applications** that require a full OS environment.
- Offers better security due to **hardware-level virtualization**.

**Disadvantages of Virtual Machines**

- **High resource consumption** (CPU, RAM, and disk space).
- **Slower startup time** compared to containers.
- Requires more storage for OS images and virtual disks.
- Management and maintenance are more complex.

**Advantages of Containers**

- **Lightweight and fast** as containers share the host OS kernel.
- **Quick startup and shutdown**, ideal for rapid deployment.
- Efficient use of **system resources**.
- Well-suited for **microservices and cloud-native applications**.

**Disadvantages of Containers**

- **Weaker isolation** compared to virtual machines.
- Dependent on the **host operating system kernel**.
- Less suitable for applications requiring a full OS environment.
- Security risks if containers are not properly configured.

**Experiment Setup - Part A: Virtual Machine (Windows)**

**Step 1: Install VirtualBox**

- Download VirtualBox from the official website.
- Run the installer and keep default options.
- Restart the system if prompted.
  
![](Lab/EXPERIMENT 1/virtual.png)

**Step 2: Install Vagrant**

- Download Vagrant for Windows.
- Install using default settings.
- Verify installation:

![](Lab/EXPERIMENT 1/vagrant.png)

```Code : vagrant --version```

![](Lab/EXPERIMENT 1/version.png)

**Step 3: Create Ubuntu VM using Vagrant**

- Initialize Vagrant with Ubuntu box:

```Code: vagrant init hashicorp/bionic64```

- Start the VM

```Code: vagrant up```

![](Lab/EXPERIMENT 1/vm.png)

When you run vagrant init hashicorp/bionic64, Vagrant creates a configuration file called **Vagrantfile** inside the project folder. This file contains all the instructions needed to create a virtual machine. In hashicorp/bionic64, **HashiCorp** is the publisher of the Vagrant box, **bionic** refers to **Ubuntu 18.04 LTS (Bionic Beaver)**, and **64** indicates that it is a 64-bit operating system.

When you run vagrant up, Vagrant reads the **Vagrantfile** and communicates with **VirtualBox** (or another configured provider). If the required Ubuntu image is not already available on the system, Vagrant automatically downloads the box. It then creates a virtual machine, allocates system resources such as **CPU, RAM, and network settings**, and finally boots the **Ubuntu virtual machine**, making it ready for use.

![](Lab/EXPERIMENT 1/vmbox.png)

- Access the VM:

```Code: vagrant ssh```

**What's happening?**

- Vagrant connects you to the VM using **SSH**
- You enter the Ubuntu terminal **without password**
- You are now **inside the virtual machine**

**Step 4: Install Nginx inside VM**
```
Code:

- sudo apt update
- sudo apt install -y nginx
- sudo systemctl start nginx
```
![](Lab/EXPERIMENT 1/Nginx.png)

```Code: time systemctl start nginx```

**What this command does (combined explanation)**

**systemctl start nginx**

- This command tells **systemd** (Linux service manager) to **start the Nginx web server service** on the system.
- The time keyword measures **how long the command takes to execute**.

**Starts the Nginx service and measures the time taken to start it.**

**Step 5: Verify Nginx**

```Code: curl localhost```

**Stop and remove vm**
```
Code:

- vagrant halt
- vagrant destroy
```
![](Lab/EXPERIMENT 1/rm.png)

**Experiment Setup - Part B: Containers using WSL (Windows)**

**Step 1: Install WSL 2**

```Code: wsl --install```

**Verify installation**

```Code: wsl --version```

![](Lab/EXPERIMENT 1/wslversion.png)

**Step 2: Install Ubuntu on WSL**

```Code: wsl --install -d Ubuntu```

**Verify installation**

```Code: wsl -l -v```

![](Lab/EXPERIMENT 1/wslverify.png)

**Step 3: Install Docker Engine inside WSL**

```
Code:

- sudo apt update
- sudo apt install -y docker.io
- sudo systemctl start docker
- sudo usermod -aG docker \$USER
- verify installation
```
![](Lab/EXPERIMENT 1/docker.png)

**Step 4: Run Ubuntu Container with Nginx**

```Code: docker pull ubuntu```


![](Lab/EXPERIMENT 1/ubuntu.png)

**docker run -d -p 8080:80 --name nginx-container nginx**

Docker pull ubuntu: This command **downloads the Ubuntu Linux image** from Docker Hub to your system.

Docker run -d -p 8080:80 -name nginx-container nginx: It **creates and runs an Nginx container in the background** and maps it to **port 8080** on your system.

**Step 5: Verify Nginx in Container**

```Code: curl localhost:8080```

![](Lab/EXPERIMENT 1/verifynginx.png)

**Resource Utilization Observation**

**VM Observation Commands**

```Code: free -h```

**What it does:**

- Displays **memory (RAM) usage** of the system

**What it shows:**

Total RAM Used RAM Free RAM Available RAM Swap memory

![](Lab/EXPERIMENT 1/resource.png)

```Code: htop```

**What it does:**

- Shows **real-time system performance**

**What it displays:**

CPU usage RAM usage Running processes Process IDs, users, load average

![](Lab/EXPERIMENT 1/realtime.png)

```Code: systemd-analyze```

![](Lab/EXPERIMENT 1/systemd.png)

**What it does:**

- Measures **system boot time**

**What it shows:**

- Time taken by:
  - Kernel
  - Userspace
- Total boot time

**Container Observation Commands**

```Code: docker stats```

**What it does:**

- Shows **real-time resource usage** of running containers

**What you'll see:**

CPU usage Memory usage / limit Network I/O Disk I/O

![](Lab/EXPERIMENT 1/dockerstats.png)

```Code: free -h```

**What this command does**

- Displays the **system's memory (RAM) usage**
- Shows how much memory is:
  - Total Used Free Available Swap

The -h flag means **human-readable** (MB / GB instead of bytes).

![](Lab/EXPERIMENT 1/free.png)

**Parameters to Compare: Virtual Machine vs Container**

| **Parameter** | **Virtual Machine** | **Container** |
| --- | --- | --- |
| **Boot Time** | High | Very Low |
| **RAM Usage** | High | Low |
| **CPU Overhead** | Higher | Minimal |
| **Disk Usage** | Larger | Smaller |
| **Isolation** | Strong | Moderate |

**Explanation of Each Parameter**

**Boot Time**

- **Virtual Machine:** Takes more time to start because it boots a full operating system.
- **Container:** Starts almost instantly since it shares the host OS kernel.

**RAM Usage**

- **Virtual Machine:** Requires dedicated memory for its own OS and services.
- **Container:** Uses less memory as it shares system resources with the host.

**CPU Overhead**

- **Virtual Machine:** More CPU usage due to hardware virtualization.
- **Container:** Minimal overhead because applications run directly on the host kernel.

**Disk Usage**

- **Virtual Machine:** Needs large disk space for OS image and virtual disks.
- **Container:** Lightweight images consume less storage.

**Isolation**

- **Virtual Machine:** Strong isolation as each VM runs its own OS.
- **Container:** Moderate isolation since containers share the host OS kernel.

**Conclusion**

Virtual Machines are suitable for full OS isolation and legacy workloads, whereas Containers are ideal for microservices, rapid deployment, and efficient resource utilization.



<div style='page-break-after: always;'></div>




## Name: Sourabh Saini






Roll no: R2142230968
Sap-ID: 500124739
School of Computer Science,

University of Petroleum and Energy Studies, Dehradun


## EXPERIMENT – 2
Docker Installation, Configuration, and Running Images

## Aim
To install and configure Docker, pull Docker images, run containers and manage
the container lifecycle using Docker commands.
## Objectives
 To pull Docker images from Docker Hub
 To run containers with port mapping
 To verify running containers
 To manage container lifecycle (start, stop, remove)

## Theory
Docker is an open-source containerization platform that allows applications to
be packaged along with their dependencies into lightweight, portable containers.
Containers run on a shared operating system kernel, making them faster and
more resource-efficient than traditional virtual machines.








A Docker Image is a read-only template used to create containers.
A Docker Container is a running instance of a Docker image.
Docker uses a client–server architecture, where the Docker client
communicates with the Docker daemon to build, run, and manage containers.

## Software Requirements
 Windows OS
 Docker Desktop with WSL integration
 Ubuntu (WSL distribution)

Procedure / Steps to Perform the Experiment

## Step 1: Pull Docker Image
The Nginx image is pulled from Docker Hub using the following command:
docker pull nginx
![](Lab/EXPERIMENT 2/Dockerpull.png)


This command downloads the latest official Nginx image to the local system.

## Step 2: Run Container with Port Mapping
Run the Nginx container in detached mode with port mapping:
docker run -d -p 8080:80 nginx
![](Lab/EXPERIMENT 2/Dockerrun.png)

## Explanation:
 -d → Runs container in background
 -p 8080:80 → Maps host port 8080 to container port 80
 nginx → Docker image name

## Step 3: Verify Running Containers
To check running containers, execute:
docker ps


![](Lab/EXPERIMENT 2/Dockerps.png)

This displays the container ID, image name, status, and port mapping.

Step 4: Stop and Remove Container
To stop the running container:
docker stop <container_id>

![](Lab/EXPERIMENT 2/Dockerstop.png)


To remove the container:
docker rm <container_id>

![](Lab/EXPERIMENT 2/Dockerdesktopcontainers.png)




Step 5: Remove Docker Image To remove the downloaded image:
docker rmi nginx
![](Lab/EXPERIMENT 2/dockerdesktop_image_removed.png)



This frees disk space by deleting the unused image.

## Result
Docker images were successfully pulled, containers were executed, and container
lifecycle management commands were performed successfully.
## Conclusion
This experiment demonstrated the use of Docker for application deployment
using containers. Docker provides a lightweight, efficient, and portable environ
ment for running applications, making it suitable for modern DevOps and cloud-
native applications.











Viva-Voce Questions (Very Important)
- What is a Docker image?
- What is a Docker container?
- Difference between docker run and docker start?
- Purpose of port mapping in Docker?
- Why are containers lightweight compared to VMs?

## Overall Conclusion
This lab demonstrated virtualization using Vagrant + VirtualBox and
containerization using Docker, highlighting clear performance and resource
efficiency differences. Containers are better suited for rapid deployment and
microservices, while VMs provide stronger isolation.



<div style='page-break-after: always;'></div>


#  Deploying NGINX Using Different Base Images and Comparing Docker Image Layers

---
## Name:Sourabh Saini






Roll no: R2142230968
Sap-ID: 500124739
School of Computer Science,

University of Petroleum and Energy Studies, Dehradun


##  Experiment 3
Deploying NGINX Web Server Using Official, Ubuntu, and Alpine Base Images and Comparing Image Layers

---

##  Aim

To deploy the NGINX web server using different Docker base images and compare their image size, performance, layers, and security impact.

---

##  Objectives

After completing this experiment, students will be able to:

- Deploy NGINX using Docker containers
- Build custom images using Dockerfile
- Understand Docker image layers
- Compare Ubuntu, Alpine, and Official images
- Analyze size, speed, and security differences
- Explain real-world uses of NGINX in containers

---

##  Prerequisites

- Docker installed and running
- Basic Linux commands
- Knowledge of:
  - docker pull
  - docker run
  - docker build
  - Dockerfile
  - Port mapping

---

#  Theory

## What is NGINX?

NGINX is a high-performance:

- Web Server
- Reverse Proxy
- Load Balancer
- API Gateway

It uses an **event-driven asynchronous architecture**, making it faster and more scalable than traditional servers like Apache.

---

## What is Docker?

Docker is a containerization platform that:

- Packages applications with dependencies
- Ensures portability
- Provides lightweight virtualization
- Speeds up deployment

---

## What are Docker Image Layers?

Docker images are built in layers.

Each instruction in Dockerfile creates a layer:

- FROM
- RUN
- COPY
- ADD

### Importance of Layers

- More layers → bigger image
- Bigger images → slower pull time
- Larger images → more vulnerabilities
- Fewer layers → faster and more secure

---

## Base Image Types

| Base Image | Description |
|-----------|-------------|
| Official nginx | Pre-built optimized production image |
| Ubuntu | Full Linux OS with tools |
| Alpine | Lightweight minimal Linux |

---

#  Experiment Procedure

---

#  Part 1 — Deploy NGINX Using Official Image

## Step 1: Pull Image

```bash
docker pull nginx:latest
```
![](Lab/EXPERIMENT 3/Dockerpull.png)

## Step 2: Run Container

```bash
docker run -d --name nginx-official -p 8080:80 nginx
```
![](Lab/EXPERIMENT 3/Dockerrun.png)
## Step 3: Verify

```bash
curl http://localhost:8080
```
![](Lab/EXPERIMENT 3/Verify.png)

OR open browser:

```
http://localhost:8080
```

---

## Observations

```bash
docker images nginx
```

- Pre-optimized
- Minimal configuration
- Production ready
- Medium size (~140MB)

---

#  Part 2 — Custom NGINX Using Ubuntu Base Image

---

## Step 1: Create Dockerfile

Create a file named `Dockerfile`:

```Dockerfile
FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y nginx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

---

## Step 2: Build Image

```bash
docker build -t nginx-ubuntu .
```
![](Lab/EXPERIMENT 3/Buildimage.png)
---

## Step 3: Run Container

```bash
docker run -d --name nginx-ubuntu -p 8081:80 nginx-ubuntu
```
![](Lab/EXPERIMENT 3/Dockerun.png)
---

## Observations

```bash
docker images nginx-ubuntu
```

- Large image (~220MB+)
- Many layers
- Includes full OS
- Slower startup
- Larger attack surface

![](Lab/EXPERIMENT 3/Dockerimages.png)

---

#  Part 3 — Custom NGINX Using Alpine Base Image

---

## Step 1: Create Dockerfile

```Dockerfile
FROM alpine:latest

RUN apk add --no-cache nginx

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

---

## Step 2: Build Image

```bash
docker build -t nginx-alpine .
```
![](Lab/EXPERIMENT 3/Dockerbuild.png)
---

## Step 3: Run Container

```bash
docker run -d --name nginx-alpine -p 8082:80 nginx-alpine
```
![](Lab/EXPERIMENT 3/Dockeruncontainer.png)
---

## Observations

```bash
docker images nginx-alpine
```

- Very small (~25–30MB)
- Minimal dependencies
- Faster pull time
- Faster startup
- More secure

---

#  Part 4 — Compare Image Sizes

## Command

```bash
docker images | grep nginx
```
![](Lab/EXPERIMENT 3/Compareimages.png)

## Sample Output

| Image Type   | Size      |
|--------------|-----------|
| nginx:latest | ~140MB    |
| nginx-ubuntu | ~220MB+   |
| nginx-alpine | ~25MB     |

---

#  Part 5 — Inspect Image Layers

## Commands

```bash
docker history nginx
docker history nginx-ubuntu
docker history nginx-alpine
```

## Observations

- Ubuntu → many filesystem layers
- Alpine → minimal layers
- Official → optimized layers

---

#  Part 6 — Serve Custom HTML Page

## Step 1: Create HTML

```bash
mkdir html
echo "<h1>Hello from Docker NGINX</h1>" > html/index.html
```
![](Lab/EXPERIMENT 3/Createhtml.png)

## Step 2: Run

```bash
docker run -d \
  -p 8083:80 \
  -v $(pwd)/html:/usr/share/nginx/html \
  nginx
```

## Step 3: Verify

Open:

```
http://localhost:8083
```
![](Lab/EXPERIMENT 3/runandverify.png)
---

#  Part 7 — Real World Uses of NGINX

NGINX is commonly used for:

- Static websites
- Reverse proxy
- Load balancing
- SSL termination
- API gateway
- Kubernetes ingress controller
- Microservices frontend

---

# Comparison Summary

| Feature | Official | Ubuntu | Alpine |
|-----------|------------|-----------|-----------|
| Size | Medium | Large | Very Small |
| Startup | Fast | Slow | Very Fast |
| Security | Medium | Low | High |
| Debugging | Limited | Good | Minimal |
| Production | Yes | Rare | Yes |

---

#  When to Use What

## Official Image
- Production deployments
- Reverse proxy
- Standard hosting

## Ubuntu Image
- Learning purposes
- Debugging tools required
- Heavy dependencies

## Alpine Image
- Cloud environments
- Microservices
- CI/CD
- Kubernetes

---

#  Assignment Tasks

1. Measure image pull time
2. Add custom NGINX configuration
3. Change default port
4. Enable basic authentication
5. Reduce layers and rebuild
6. Explain:
   - Why Alpine is smaller
   - Why Ubuntu is not preferred in production

---

#  Viva Questions

1. What is NGINX?
2. What is Docker?
3. What are Docker layers?
4. Why are Alpine images smaller?
5. Difference between Ubuntu and Alpine?
6. Why use official images in production?
7. What is reverse proxy?
8. How does NGINX improve performance?

---

#  Learning Outcomes

After completing this experiment, students can:

- Deploy web servers in containers
- Build custom Docker images
- Optimize image size
- Understand layer structure
- Improve security practices
- Use NGINX in production systems

---

#  Conclusion

This experiment demonstrates that:

- Official images are stable and production ready
- Ubuntu images are large and slower
- Alpine images are lightweight, faster, and secure

Therefore, Alpine or Official images are preferred for real-world deployments.

---

#  End of Experiment


<div style='page-break-after: always;'></div>



# **Experiment 4: Docker Essentials**

## Name: Sourabh Saini





Roll no: R2142230968
Sap-ID: 500124739
School of Computer Science,

University of Petroleum and Energy Studies, Dehradun

## **Part 1: Containerizing Applications with Dockerfile**

### **Step 1: Create a Simple Application**

**Python Flask App:**
```bash
mkdir my-flask-app
cd my-flask-app
```

**`app.py`:**
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Docker!"

@app.route('/health')
def health():
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
![](Lab/EXPERIMENT 4/main.py.png)
**`requirements.txt`:**
```
Flask==2.3.3
```

### **Step 2: Create Dockerfile**

**`Dockerfile`:**
```dockerfile
# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
```
![](Lab/EXPERIMENT 4/Dockerfile.png)
---

## **Part 2: Using .dockerignore**

### **Step 1: Create .dockerignore File**

**`.dockerignore`:**
```
# Python files
__pycache__/
*.pyc
*.pyo
*.pyd

# Environment files
.env
.venv
env/
venv/

# IDE files
.vscode/
.idea/

# Git files
.git/
.gitignore

# OS files
.DS_Store
Thumbs.db

# Logs
*.log
logs/

# Test files
tests/
test_*.py
```

### **Step 2: Why .dockerignore is Important**
- Prevents unnecessary files from being copied
- Reduces image size
- Improves build speed
- Increases security

---

## **Part 3: Building Docker Images**

### **Step 1: Basic Build Command**
```bash
# Build image from Dockerfile
docker build -t my-flask-app .

# Check built images
docker images
```

### **Step 2: Tagging Images**

```bash
# Tag with version number
docker build -t my-flask-app:1.0 .

# Tag with multiple tags
docker build -t my-flask-app:latest -t my-flask-app:1.0 .

# Tag with custom registry
docker build -t username/my-flask-app:1.0 .

# Tag existing image
docker tag my-flask-app:latest my-flask-app:v1.0
```
![](Lab/EXPERIMENT 4/Dockerbuild.png)

### **Step 3: View Image Details**
```bash
# List all images
docker images

# Show image history
docker history my-flask-app

# Inspect image details
docker inspect my-flask-app
```

---

## **Part 4: Running Containers**

### **Step 1: Run Container**
```bash
# Run container with port mapping
docker run -d -p 5000:5000 --name flask-container my-flask-app

# Test the application
curl http://localhost:5000

# View running containers
docker ps

# View container logs
docker logs flask-container
```
![](Lab/EXPERIMENT 4/Dockerrun.png)

![](Lab/EXPERIMENT 4/image-2.png)
### **Step 2: Manage Containers**
```bash
# Stop container
docker stop flask-container

# Start stopped container
docker start flask-container

# Remove container
docker rm flask-container

# Remove container forcefully
docker rm -f flask-container
```

---

## **Part 5: Multi-stage Builds**

### **Step 1: Why Multi-stage Builds?**
- Smaller final image size
- Better security (remove build tools)
- Separate build and runtime environments

### **Step 2: Simple Multi-stage Dockerfile**

**`Dockerfile.multistage`:**
```dockerfile
# STAGE 1: Builder stage
FROM python:3.9-slim AS builder

WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies in virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --no-cache-dir -r requirements.txt

# STAGE 2: Runtime stage
FROM python:3.9-slim

WORKDIR /app

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy application code
COPY app.py .

# Create non-root user
RUN useradd -m -u 1000 appuser
USER appuser

# Expose port
EXPOSE 5000

# Run application
CMD ["python", "app.py"]
```
![](Lab/EXPERIMENT 4/Dockermultistage.png)

### **Step 3: Build and Compare**
```bash
# Build regular image
docker build -t flask-regular .

# Build multi-stage image
docker build -f Dockerfile.multistage -t flask-multistage .

# Compare sizes
docker images | grep flask-

# Expected output:
# flask-regular     ~250MB
# flask-multistage  ~150MB (40% smaller!)
```
![](Lab/EXPERIMENT 4/dockerbuild2.png)
![](Lab/EXPERIMENT 4/dockerimges2.png)
---

## **Part 6: Publishing to Docker Hub**

### **Step 1: Prepare for Publishing**
```bash
# Login to Docker Hub
docker login

# Tag image for Docker Hub
docker tag my-flask-app:latest username/my-flask-app:1.0
docker tag my-flask-app:latest username/my-flask-app:latest

# Push to Docker Hub
docker push username/my-flask-app:1.0
docker push username/my-flask-app:latest
```
![](Lab/EXPERIMENT 4/imagetag.png)
![](Lab/EXPERIMENT 4/imagepush.png)
![](Lab/EXPERIMENT 4/repository.png)
### **Step 2: Pull and Run from Docker Hub**
```bash
# Pull from Docker Hub (on another machine)
docker pull username/my-flask-app:latest

# Run the pulled image
docker run -d -p 5000:5000 username/my-flask-app:latest
```
![](Lab/EXPERIMENT 4/Dockerpull.png)
![](Lab/EXPERIMENT 4/run5000.png)
---

## **Part 7: Node.js Example (Quick Version)**

### **Step 1: Node.js Application**
```bash
mkdir my-node-app
cd my-node-app

```
![](Lab/EXPERIMENT 4/nodeapp.png)
**`app.js`:**
```javascript
const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
    res.send('Hello from Node.js Docker!');
});

app.get('/health', (req, res) => {
    res.json({ status: 'healthy' });
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
```
![](Lab/EXPERIMENT 4/app.js.png)

**`package.json`:**
```json
{
  "name": "node-docker-app",
  "version": "1.0.0",
  "main": "app.js",
  "dependencies": {
    "express": "^4.18.2"
  }
}
```
![](Lab/EXPERIMENT 4/package.png)
### **Step 2: Node.js Dockerfile**
```dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install --only=production

COPY app.js .

EXPOSE 3000

CMD ["node", "app.js"]
```
![](Lab/EXPERIMENT 4/image-4.png)
### **Step 3: Build and Run**
```bash
# Build image
docker build -t my-node-app .

# Run container
docker run -d -p 3000:3000 --name node-container my-node-app

# Test
curl http://localhost:3000
```

---

![](Lab/EXPERIMENT 4/image-5.png)
![](Lab/EXPERIMENT 4/image-6.png)
![](Lab/EXPERIMENT 4/testnodeapp.png)
---

## **Essential Docker Commands Cheatsheet**

| Command | Purpose | Example |
|---------|---------|---------|
| `docker build` | Build image | `docker build -t myapp .` |
| `docker run` | Run container | `docker run -p 3000:3000 myapp` |
| `docker ps` | List containers | `docker ps -a` |
| `docker images` | List images | `docker images` |
| `docker tag` | Tag image | `docker tag myapp:latest myapp:v1` |
| `docker login` | Login to Dockerhub using username and password or token | `echo "token" | docker login -u username --password-stdin` |
| `docker push` | Push to registry | `docker push username/myapp` |
| `docker pull` | Pull from registry | `docker pull username/myapp` |
| `docker rm` | Remove container | `docker rm container-name` |
| `docker rmi` | Remove image | `docker rmi image-name` |
| `docker logs` | View logs | `docker logs container-name` |
| `docker exec` | Execute command | `docker exec -it container-name bash` |

---

## **Common Workflow Summary**

### **Development Workflow:**
```bash
# 1. Create Dockerfile and .dockerignore
# 2. Build image
docker build -t myapp .

# 3. Test locally
docker run -p 8080:8080 myapp

# 4. Tag for production
docker tag myapp:latest myapp:v1.0

# 5. Push to registry
docker push myapp:v1.0
```

### **Production Workflow:**
```bash
# 1. Pull from registry
docker pull myapp:v1.0

# 2. Run in production
docker run -d -p 80:8080 --name prod-app myapp:v1.0

# 3. Monitor
docker logs -f prod-app
```

---

## **Key Takeaways**

1. **Dockerfile** defines how to build your image
2. **.dockerignore** excludes unnecessary files (important for security and performance)
3. **Tagging** helps version and organize images
4. **Multi-stage builds** create smaller, more secure production images
5. **Docker Hub** allows sharing and distributing images
6. **Always test** images locally before publishing

---

## **Cleanup**
```bash
# Remove all stopped containers
docker container prune

# Remove unused images
docker image prune

# Remove everything unused
docker system prune -a
```
# **Experiment 4: Docker Essentials**

## Name: Sourabh Saini






Roll no: R2142230968
Sap-ID: 500124739
School of Computer Science,

University of Petroleum and Energy Studies, Dehradun

## **Part 1: Containerizing Applications with Dockerfile**

### **Step 1: Create a Simple Application**

**Python Flask App:**
```bash
mkdir my-flask-app
cd my-flask-app
```

**`app.py`:**
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Docker!"

@app.route('/health')
def health():
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
![](Lab/EXPERIMENT 4/main.py.png)
**`requirements.txt`:**
```
Flask==2.3.3
```

### **Step 2: Create Dockerfile**

**`Dockerfile`:**
```dockerfile
# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
```
![](Lab/EXPERIMENT 4/Dockerfile.png)
---

## **Part 2: Using .dockerignore**

### **Step 1: Create .dockerignore File**

**`.dockerignore`:**
```
# Python files
__pycache__/
*.pyc
*.pyo
*.pyd

# Environment files
.env
.venv
env/
venv/

# IDE files
.vscode/
.idea/

# Git files
.git/
.gitignore

# OS files
.DS_Store
Thumbs.db

# Logs
*.log
logs/

# Test files
tests/
test_*.py
```

### **Step 2: Why .dockerignore is Important**
- Prevents unnecessary files from being copied
- Reduces image size
- Improves build speed
- Increases security

---

## **Part 3: Building Docker Images**

### **Step 1: Basic Build Command**
```bash
# Build image from Dockerfile
docker build -t my-flask-app .

# Check built images
docker images
```

### **Step 2: Tagging Images**

```bash
# Tag with version number
docker build -t my-flask-app:1.0 .

# Tag with multiple tags
docker build -t my-flask-app:latest -t my-flask-app:1.0 .

# Tag with custom registry
docker build -t username/my-flask-app:1.0 .

# Tag existing image
docker tag my-flask-app:latest my-flask-app:v1.0
```
![](Lab/EXPERIMENT 4/Dockerbuild.png)

### **Step 3: View Image Details**
```bash
# List all images
docker images

# Show image history
docker history my-flask-app

# Inspect image details
docker inspect my-flask-app
```

---

## **Part 4: Running Containers**

### **Step 1: Run Container**
```bash
# Run container with port mapping
docker run -d -p 5000:5000 --name flask-container my-flask-app

# Test the application
curl http://localhost:5000

# View running containers
docker ps

# View container logs
docker logs flask-container
```
![](Lab/EXPERIMENT 4/Dockerrun.png)

![](Lab/EXPERIMENT 4/image-2.png)
### **Step 2: Manage Containers**
```bash
# Stop container
docker stop flask-container

# Start stopped container
docker start flask-container

# Remove container
docker rm flask-container

# Remove container forcefully
docker rm -f flask-container
```

---

## **Part 5: Multi-stage Builds**

### **Step 1: Why Multi-stage Builds?**
- Smaller final image size
- Better security (remove build tools)
- Separate build and runtime environments

### **Step 2: Simple Multi-stage Dockerfile**

**`Dockerfile.multistage`:**
```dockerfile
# STAGE 1: Builder stage
FROM python:3.9-slim AS builder

WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies in virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --no-cache-dir -r requirements.txt

# STAGE 2: Runtime stage
FROM python:3.9-slim

WORKDIR /app

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy application code
COPY app.py .

# Create non-root user
RUN useradd -m -u 1000 appuser
USER appuser

# Expose port
EXPOSE 5000

# Run application
CMD ["python", "app.py"]
```
![](Lab/EXPERIMENT 4/Dockermultistage.png)

### **Step 3: Build and Compare**
```bash
# Build regular image
docker build -t flask-regular .

# Build multi-stage image
docker build -f Dockerfile.multistage -t flask-multistage .

# Compare sizes
docker images | grep flask-

# Expected output:
# flask-regular     ~250MB
# flask-multistage  ~150MB (40% smaller!)
```
![](Lab/EXPERIMENT 4/dockerbuild2.png)
![](Lab/EXPERIMENT 4/dockerimges2.png)
---

## **Part 6: Publishing to Docker Hub**

### **Step 1: Prepare for Publishing**
```bash
# Login to Docker Hub
docker login

# Tag image for Docker Hub
docker tag my-flask-app:latest username/my-flask-app:1.0
docker tag my-flask-app:latest username/my-flask-app:latest

# Push to Docker Hub
docker push username/my-flask-app:1.0
docker push username/my-flask-app:latest
```
![](Lab/EXPERIMENT 4/imagetag.png)
![](Lab/EXPERIMENT 4/imagepush.png)
![](Lab/EXPERIMENT 4/repository.png)
### **Step 2: Pull and Run from Docker Hub**
```bash
# Pull from Docker Hub (on another machine)
docker pull username/my-flask-app:latest

# Run the pulled image
docker run -d -p 5000:5000 username/my-flask-app:latest
```
![](Lab/EXPERIMENT 4/Dockerpull.png)
![](Lab/EXPERIMENT 4/run5000.png)
---

## **Part 7: Node.js Example (Quick Version)**

### **Step 1: Node.js Application**
```bash
mkdir my-node-app
cd my-node-app

```
![](Lab/EXPERIMENT 4/nodeapp.png)
**`app.js`:**
```javascript
const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
    res.send('Hello from Node.js Docker!');
});

app.get('/health', (req, res) => {
    res.json({ status: 'healthy' });
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
```
![](Lab/EXPERIMENT 4/app.js.png)

**`package.json`:**
```json
{
  "name": "node-docker-app",
  "version": "1.0.0",
  "main": "app.js",
  "dependencies": {
    "express": "^4.18.2"
  }
}
```
![](Lab/EXPERIMENT 4/package.png)
### **Step 2: Node.js Dockerfile**
```dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install --only=production

COPY app.js .

EXPOSE 3000

CMD ["node", "app.js"]
```
![](Lab/EXPERIMENT 4/image-4.png)
### **Step 3: Build and Run**
```bash
# Build image
docker build -t my-node-app .

# Run container
docker run -d -p 3000:3000 --name node-container my-node-app

# Test
curl http://localhost:3000
```

---

![](Lab/EXPERIMENT 4/image-5.png)
![](Lab/EXPERIMENT 4/image-6.png)
![](Lab/EXPERIMENT 4/testnodeapp.png)
---

## **Essential Docker Commands Cheatsheet**

| Command | Purpose | Example |
|---------|---------|---------|
| `docker build` | Build image | `docker build -t myapp .` |
| `docker run` | Run container | `docker run -p 3000:3000 myapp` |
| `docker ps` | List containers | `docker ps -a` |
| `docker images` | List images | `docker images` |
| `docker tag` | Tag image | `docker tag myapp:latest myapp:v1` |
| `docker login` | Login to Dockerhub using username and password or token | `echo "token" | docker login -u username --password-stdin` |
| `docker push` | Push to registry | `docker push username/myapp` |
| `docker pull` | Pull from registry | `docker pull username/myapp` |
| `docker rm` | Remove container | `docker rm container-name` |
| `docker rmi` | Remove image | `docker rmi image-name` |
| `docker logs` | View logs | `docker logs container-name` |
| `docker exec` | Execute command | `docker exec -it container-name bash` |

---

## **Common Workflow Summary**

### **Development Workflow:**
```bash
# 1. Create Dockerfile and .dockerignore
# 2. Build image
docker build -t myapp .

# 3. Test locally
docker run -p 8080:8080 myapp

# 4. Tag for production
docker tag myapp:latest myapp:v1.0

# 5. Push to registry
docker push myapp:v1.0
```

### **Production Workflow:**
```bash
# 1. Pull from registry
docker pull myapp:v1.0

# 2. Run in production
docker run -d -p 80:8080 --name prod-app myapp:v1.0

# 3. Monitor
docker logs -f prod-app
```

---

## **Key Takeaways**

1. **Dockerfile** defines how to build your image
2. **.dockerignore** excludes unnecessary files (important for security and performance)
3. **Tagging** helps version and organize images
4. **Multi-stage builds** create smaller, more secure production images
5. **Docker Hub** allows sharing and distributing images
6. **Always test** images locally before publishing

---

## **Cleanup**
```bash
# Remove all stopped containers
docker container prune

# Remove unused images
docker image prune

# Remove everything unused
docker system prune -a
```




<div style='page-break-after: always;'></div>



# Experiment 5: Docker - Volumes, Environment Variables, Monitoring & Networks

## Part 1: Docker Volumes - Persistent Data Storage

### Lab 1: Understanding Data Persistence

**The Problem: Container Data is Ephemeral**
```bash 
# Create a container that writes data
docker run -it --name test-container ubuntu /bin/bash
# Inside container:
echo "Hello World" > /data/message.txt
cat /data/message.txt # Shows "Hello World"
exit

# Restart container
docker start test-container
docker exec test-container cat /data/message.txt
# ERROR: File doesn't exist! Data was lost.
Solution: Docker Volumes
```

![](Lab/EXPERIMENT 5/image.png)

## Lab 2: Volume Types

```bash
# Create anonymous volume (auto-generated name)
docker run -d -v /app/data --name web1 nginx
# Check volume
docker volume ls
# Inspect container to see volume mount
docker inspect web1 | grep -A 5 Mounts

2. Named Volumes
Bash
# Create named volume
docker volume create mydata

# Use named volume
docker run -d -v mydata:/app/data --name web2 nginx

# List volumes
docker volume ls
# Shows: mydata

# Inspect volume
docker volume inspect mydata
```
![](Lab/EXPERIMENT 5/image-2.png)
3. Bind Mounts (Host Directory)
```Bash
# Create directory on host
mkdir ~/myapp-data

# Mount host directory to container
docker run -d -v ~/myapp-data:/app/data --name web3 nginx

# Add file on host
echo "From Host" > ~/myapp-data/host-file.txt

# Check in container
docker exec web3 cat /app/data/host-file.txt
# Shows: From Host
```

![](Lab/EXPERIMENT 5/image-1.png)

### Lab 3: Practical Volume Examples
Example 1: Database with Persistent Storage

```Bash
# MySQL with named volume
docker run -d \
  --name mysql-db \
  -v mysql-data:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD=secret \
  mysql:8.0

# Check data persists
docker stop mysql-db
docker rm mysql-db

# New container with same volume
docker run -d \
  --name new-mysql \
  -v mysql-data:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD=secret \
  mysql:8.0
# Data is preserved!
```

Example 2: Web App with Configuration Files
```Bash

# Create config directory
mkdir ~/nginx-config

# Create nginx config file
echo 'server {
    listen 80;
    server_name localhost;
    location / {
        return 200 "Hello from mounted config!";
    }
}' > ~/nginx-config/nginx.conf

# Run nginx with config bind mount
docker run -d \
  --name nginx-custom \
  -p 8080:80 \
  -v ~/nginx-config/nginx.conf:/etc/nginx/conf.d/default.conf \
  nginx

# Test
curl http://localhost:8080
```
![](Lab/EXPERIMENT 5/image-3.png)

Lab 4: Volume Management Commands
```Bash
# List all volumes
docker volume ls

# Create a volume
docker volume create app-volume

# Inspect volume details
docker volume inspect app-volume

# Remove unused volumes
docker volume prune

# Remove specific volume
docker volume rm volume-name

# Copy files to/from volume
docker cp local-file.txt container-name:/path/in/volume

```
![](Lab/EXPERIMENT 5/image-4.png)
![](Lab/EXPERIMENT 5/textfile.png)

## Part 2: Environment Variables
Lab 1: Setting Environment Variables
## Method 1: Using -e flag

```Bash
# Single variable
docker run -d \
  --name app1 \
  -e DATABASE_URL="postgres://user:pass@db:5432/mydb" \
  -e DEBUG="true" \
  -p 3000:3000 \
  my-node-app

# Multiple variables
docker run -d \
  -e VAR1=value1 \
  -e VAR2=value2 \
  -e VAR3=value3 \
  my-app
```

### Method 2: Using --env-file
``` Bash
# Create .env file
echo "DATABASE_HOST=localhost" > .env
echo "DATABASE_PORT=5432" >> .env
echo "API_KEY=secret123" >> .env

# Use env file
docker run -d \
  --env-file .env \
  --name app2 \
  my-app

# Use multiple env files
docker run -d \
  --env-file .env \
  --env-file .env.secrets \
  my-app
```
![](Lab/EXPERIMENT 5/image-7.png)
### Method 3: In Dockerfile
```Bash
# Set default environment variables
ENV NODE_ENV=production
ENV PORT=3000
ENV APP_VERSION=1.0.0
# Can be overridden at runtime
```
## Lab 2: Environment Variables in Applications
```Bash
Python Flask Example

app.py
import os
from flask import Flask

app = Flask(__name__)
Read environment variables
db_host = os.environ.get('DATABASE_HOST', 'localhost')
debug_mode = os.environ.get('DEBUG', 'false').lower() == 'true'
api_key = os.environ.get('API_KEY')

@app.route('/config')
def config():
    return {
        'db_host': db_host,
        'debug': debug_mode,
        'has_api_key': bool(api_key)
    }

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=debug_mode)
```
![](Lab/EXPERIMENT 5/image-5.png)

### Dockerfile with Environment Variables
```Bash

Dockerfile
FROM python:3.9-slim
Set environment variables at build time
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .

# Default runtime environment variables
ENV PORT=5000
ENV DEBUG=false

EXPOSE 5000
CMD ["python", "app.py"]
```
![](Lab/EXPERIMENT 5/image-6.png)
### Lab 3: Test Environment Variables
```Bash
# Run with custom env vars

docker run -d \
  --name flask-app \
  -p 5000:5000 \
  -e DATABASE_HOST="prod-db.example.com" \
  -e DEBUG="true" \
  -e PORT="8080" \
  flask-app

# Check environment in running container
docker exec flask-app env
docker exec flask-app printenv DATABASE_HOST

# Test the endpoint
curl http://localhost:5000/config
```
![](Lab/EXPERIMENT 5/image-8.png)
### Part 3: Docker Monitoring 
### Lab 1: Basic Monitoring Commands
### docker stats - Real-time Container Metrics

```bash
# Live stats for all containers
docker stats

# Live stats for specific containers
docker stats container1 container2

# Specific format output
docker stats --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}"

# No-stream (single snapshot)
docker stats --no-stream

# All containers (including stopped)
docker stats --all

# Useful Format Options:
# Custom format
docker stats --format "Container: {{.Name}} | CPU: {{.CPUPerc}} | Memory: {{.MemPerc}}"
# JSON output
docker stats --format json --no-stream
# Wide output
docker stats --no-stream --no-trunc

```
![](Lab/EXPERIMENT 5/image-9.png)
### Lab 2: docker top - Process Monitoring
``` Bash
# View processes in container
docker top container-name

# View with full command line
docker top container-name -ef

# Compare with host processes
ps aux | grep docker
```

### Lab 3: docker logs - Application Logs
```Bash
# View logs
docker logs container-name

# Follow logs (like tail -f)
docker logs -f container-name

# Last N lines
docker logs --tail 100 container-name

# Logs with timestamps
docker logs -t container-name

# Logs since specific time
docker logs --since 2024-01-15 container-name

# Combine options
docker logs -f --tail 50 -t container-name
```
![](Lab/EXPERIMENT 5/image-10.png)
### Lab 4: Container Inspection
```Bash
# Detailed container info
docker inspect container-name

# Specific information
docker inspect --format='{{.State.Status}}' container-name
docker inspect --format='{{.NetworkSettings.IPAddress}}' container-name
docker inspect --format='{{.Config.Env}}' container-name

# Resource limits
docker inspect --format='{{.HostConfig.Memory}}' container-name
docker inspect --format='{{.HostConfig.NanoCpus}}' container-name
Lab 5: Events Monitoring
Bash
# Monitor Docker events in real-time
docker events

# Filter events
docker events --filter 'type=container'
docker events --filter 'event=start'
docker events --filter 'event=die'

# Since specific time
docker events --since '2024-01-15'

# Format output
docker events --format '{{.Type}} {{.Action}} {{.Actor.Attributes.name}}'
```
### Lab 6: Practical Monitoring Script
```Bash

#!/bin/bash
# monitor.sh
# Simple Docker monitoring

echo "=== Docker Monitoring Dashboard ==="
echo "Time: $(date)"
echo

echo "1. Running Containers:"
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
echo

echo "2. Resource Usage:"
docker stats --no-stream --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}"
echo

echo "3. Recent Events:"
docker events --since '5m' --until '0s' --format '{{.Time}} {{.Type}} {{.Action}}' | tail -5
echo

echo "4. System Info:"
docker system df
```
### Part 4: Docker Networks
### Lab 1: Understanding Docker Network Types
```Bash
# Default networks
docker network ls

# Output:
# NETWORK ID          NAME                DRIVER              SCOPE
# abc123              bridge              bridge              local
# def456              host                host                local
# ghi789              none                null                local
Lab 2: Network Types Explained
1. Bridge Network (Default)
Bash
# Containers on bridge network can communicate
# Each container gets own IP, isolated from host

# Create custom bridge network
docker network create my-network

# Inspect network
docker network inspect my-network

# Run containers on custom network
docker run -d --name web1 --network my-network nginx
docker run -d --name web2 --network my-network nginx

# Containers can communicate using container names
docker exec web1 curl http://web2
```
![](Lab/EXPERIMENT 5/image-11.png)
### 2. Host Network
```Bash
# Container uses host's network directly
# No network isolation, shares host's IP

docker run -d --name host-app --network host nginx

# Access directly on host port 80
curl http://localhost
```
![](Lab/EXPERIMENT 5/image-12.png)

### 3. None Network
```Bash
# No network access
docker run -d --name isolated-app --network none alpine sleep 3600

# Test no network interfaces
docker exec isolated-app ifconfig

```
![](Lab/EXPERIMENT 5/image-13.png)
### 4. Overlay Network (Swarm)
```Bash
# For Docker Swarm multi-host networking
docker network create --driver overlay my-overlay
```
![](Lab/EXPERIMENT 5/image-14.png)
### Lab 3: Network Management Commands
```Bash
# Create network
docker network create app-network
docker network create --driver bridge --subnet 172.20.0.1/16 my-subnet

# Connect container to network
docker network connect app-network existing-container

# Disconnect container from network
docker network disconnect app-network container-name

# Remove network
docker network rm network-name

# Prune unused networks
docker network prune
```
![](Lab/EXPERIMENT 5/3.png)
![](Lab/EXPERIMENT 5/image-15.png)
### Lab 4: Multi-Container Application Example
Web App + Database Communication

```Bash
# Create network
docker network create app-network

# Start database
docker run -d \
  --name postgres-db \
  --network app-network \
  -e POSTGRES_PASSWORD=secret \
  -v pgdata:/var/lib/postgresql/data \
  postgres:15

# Start web application
docker run -d \
  --name web-app \
  --network app-network \
  -p 8080:3000 \
  -e DATABASE_URL="postgres://postgres:secret@postgres-db:5432/mydb" \
  -e DATABASE_HOST="postgres-db" \
  node-app

# Web app can connect to database using "postgres-db" hostname
```
![](Lab/EXPERIMENT 5/3.png)
![](Lab/EXPERIMENT 5/4.png)


### Lab 5: Network Inspection & Debugging
```Bash
# Inspect network
docker network inspect bridge

# Check container IP
docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container-name

# DNS resolution test
docker exec container-name nslookup another-container

# Network connectivity test
docker exec container-name ping -c 4 google.com
docker exec container-name curl -I http://another-container

# View network ports
docker port container-name
```
![](Lab/EXPERIMENT 5/image-17.png)

### Lab 6: Port Publishing vs Exposing
``` Bash
# PORT PUBLISHING (host:container)
docker run -d -p 80:8080 --name app1 nginx
# Host port 80 → Container port 8080

# Dynamic port publishing
docker run -d -p 8080 --name app2 nginx
# Docker assigns random host port

# Multiple ports
docker run -d -p 80:80 -p 443:443 --name app3 nginx

# Specific host IP
docker run -d -p 127.0.0.1:8080:80 --name app4 nginx

# EXPOSE in Dockerfile (metadata only)
# Dockerfile: EXPOSE 80
# Still need -p to publish
```
![](Lab/EXPERIMENT 5/image-18.png)

### Part 5: Complete Real-World Example
Application Architecture:

Flask Web App (port 5000)

PostgreSQL Database (port 5432)

Redis Cache (port 6379)

All connected via custom network

Implementation:

```Bash
# 1. Create network
docker network create myapp-network

# 2. Start database with volume
docker run -d \
  --name postgres \
  --network myapp-network \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -e POSTGRES_DB=mydatabase \
  -v postgres-data:/var/lib/postgresql/data \
  postgres:15

# 3. Start Redis
docker run -d \
  --name redis \
  --network myapp-network \
  -v redis-data:/data \
  redis:7-alpine

# 4. Start Flask app with all configurations
docker run -d \
  --name flask-app \
  --network myapp-network \
  -p 5000:5000 \
  -v $(pwd)/app:/app \
  -v app-logs:/var/log/app \
  -e DATABASE_URL="postgresql://postgres:mysecretpassword@postgres:5432/mydatabase" \
  -e REDIS_URL="redis://redis:6379" \
  -e DEBUG="false" \
  -e LOG_LEVEL="INFO" \
  --env-file .env.production \
  flask-app:latest
```
![](Lab/EXPERIMENT 5/image-20.png)
```bash
Monitoring commands 
# Check all components
docker ps

# Monitor resources
docker stats postgres redis flask-app

# Check logs
docker logs -f flask-app

# Network connectivity test
docker exec flask-app ping -c 2 postgres
docker exec flask-app ping -c 2 redis

# View network details
docker network inspect myapp-network
```
![](Lab/EXPERIMENT 5/image-21.png)
![](Lab/EXPERIMENT 5/image-19.png)
![](Lab/EXPERIMENT 5/image-16.png)



<div style='page-break-after: always;'></div>


# Experiment 6: Comparison of Docker Run and Docker Compose

**Name:** Sourabh Saini
**Roll No:** R2142230968
**Course:** Containerization and DevOps Lab
**Experiment No:** 6    

---

##  Objective

To understand the relationship between `docker run` and Docker Compose, and to compare their configuration syntax and use cases by deploying single-container and multi-container applications.

---

##  PART A – Theory

### 1. Docker Run (Imperative Approach)

The `docker run` command creates and starts a container from an image. It requires explicit flags for port mapping (`-p`), volume mounting (`-v`), environment variables (`-e`), network configuration (`--network`), restart policies (`--restart`), resource limits (`--memory`, `--cpus`), and container name (`--name`).

**Example:**
```bash
docker run -d \
  --name my-nginx \
  -p 8080:80 \
  -v ./html:/usr/share/nginx/html \
  -e NGINX_HOST=localhost \
  nginx:alpine
```
![](Lab/EXPERIMENT 6/image.png)
### 2. Docker Compose (Declarative Approach)

Docker Compose uses a YAML file (`docker-compose.yml`) to define services, networks, and volumes in a structured format. Instead of multiple commands, a single command is used: `docker compose up -d`

**Equivalent Compose file:**
```yaml
version: '3.8'
services:
  nginx:
    image: nginx:alpine
    container_name: my-nginx
    ports:
      - "8080:80"
    volumes:
      - ./html:/usr/share/nginx/html
    environment:
      NGINX_HOST: localhost
    restart: unless-stopped
```
![](Lab/EXPERIMENT 6/image-1.png)

### 3. Mapping: Docker Run vs Docker Compose

| Docker Run Flag | Docker Compose Equivalent |
|---|---|
| `-p 8080:80` | `ports:` |
| `-v host:container` | `volumes:` |
| `-e KEY=value` | `environment:` |
| `--name` | `container_name:` |
| `--network` | `networks:` |
| `--restart` | `restart:` |
| `--memory` | `deploy.resources.limits.memory` |
| `--cpus` | `deploy.resources.limits.cpus` |
| `-d` | `docker compose up -d` |

### 4. Advantages of Docker Compose

1. Simplifies multi-container applications
2. Provides reproducibility
3. Version controllable configuration
4. Unified lifecycle management
5. Supports service scaling: `docker compose up --scale web=3`

---

## 🧪 PART B – Practical Implementation

---

### Task 1: Single Container Comparison

---

#### Step 1: Run Nginx Using Docker Run

**Command:**
```bash
docker run -d \
  --name lab-nginx \
  -p 8081:80 \
  -v $(pwd)/html:/usr/share/nginx/html \
  nginx:alpine
```

![](Lab/EXPERIMENT 6/image.png)

**Verify container is running:**
```bash
docker ps
```
![](Lab/EXPERIMENT 6/image-4.png)
**Access in browser:** `http://localhost:8081`

**📸 Screenshot – Browser output (Docker Run):**

![](Lab/EXPERIMENT 6/image-2.png)



---

**Stop and remove container:**
```bash
docker stop lab-nginx
docker rm lab-nginx
```

---

#### Step 2: Run Same Setup Using Docker Compose

**Create `docker-compose.yml`:**
```yaml
version: '3.8'
services:
  nginx:
    image: nginx:alpine
    container_name: lab-nginx
    ports:
      - "8081:80"
    volumes:
      - ./html:/usr/share/nginx/html
```

**Run container:**
```bash
docker compose up -d
```
![](Lab/EXPERIMENT 6/image-3.png)
**Verify:**
```bash
docker compose ps
```
![](Lab/EXPERIMENT 6/image-5.png)
---

**Stop containers:**
```bash
docker compose down
```
##### Command Explanation:Docker compose down: Stop and remove all services, networks (but preserves volumes)
---

### Task 2: Multi-Container Application — WordPress + MySQL

---

#### Part A: Using Docker Run (Manual Method)

**Step 1: Create network:**
```bash
docker network create wp-net
```
![](Lab/EXPERIMENT 6/image-6.png)

**Step 2: Run MySQL container:**
```bash
docker run -d \
  --name mysql \
  --network wp-net \
  -e MYSQL_ROOT_PASSWORD=secret \
  -e MYSQL_DATABASE=wordpress \
  mysql:5.7
```
![](Lab/EXPERIMENT 6/image-7.png)
**Step 3: Run WordPress container:**
```bash
docker run -d \
  --name wordpress \
  --network wp-net \
  -p 8082:80 \
  -e WORDPRESS_DB_HOST=mysql \
  -e WORDPRESS_DB_PASSWORD=secret \
  wordpress:latest
```
![](Lab/EXPERIMENT 6/image-8.png)
**Verify both containers running:**
```bash
docker ps
```
![](Lab/EXPERIMENT 6/image-4.png)
**Access in browser:** `http://localhost:8082`

**📸 Screenshot – WordPress installation page (via Docker Run):**
![](Lab/EXPERIMENT 6/<Screenshot 2026-03-19 at 11.02.08 PM.png>)

![](Lab/EXPERIMENT 6/image-9.png)

> *The WordPress installation page loads at `http://localhost:8082`, confirming both the MySQL and WordPress containers are running and communicating via the `wp-net` Docker network.*

---

#### Part B: Using Docker Compose (Structured Method)

**Create `docker-compose.yml`:**
```yaml
version: '3.8'
services:
  mysql:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: secret
      MYSQL_DATABASE: wordpress
    volumes:
      - mysql_data:/var/lib/mysql

  wordpress:
    image: wordpress:latest
    ports:
      - "8082:80"
    environment:
      WORDPRESS_DB_HOST: mysql
      WORDPRESS_DB_PASSWORD: secret
    depends_on:
      - mysql

volumes:
  mysql_data:
```
![](Lab/EXPERIMENT 6/image-10.png)
**Start application:**
```bash
docker compose up -d
```
**Verify:**
```bash
docker ps
```

**Access in browser:** `http://localhost:8082`

**📸 Screenshot – WordPress page via Docker Compose:**

![](Lab/EXPERIMENT 6/<Screenshot 2026-03-19 at 11.02.08 PM.png>)

**Stop and remove everything:**
```bash
docker compose down -v
```

---

## 🔄 PART C – Conversion & Build-Based Tasks

---

### Task 3: Convert Docker Run to Docker Compose

---

#### Problem 1: Basic Web Application

**Given Docker Run command:**
```bash
docker run -d \
  --name webapp \
  -p 5000:5000 \
  -e APP_ENV=production \
  -e DEBUG=false \
  --restart unless-stopped \
  node:18-alpine
```
![](Lab/EXPERIMENT 6/image-13.png)
**Equivalent `docker-compose.yml`:**
```yaml
version: '3.8'
services:
  webapp:
    image: node:18-alpine
    container_name: webapp
    ports:
      - "5000:5000"
    environment:
      APP_ENV: production
      DEBUG: "false"
    restart: unless-stopped
```
![](Lab/EXPERIMENT 6/image-12.png)
**Run:**
```bash
docker compose up -d
```

**Verify:**
```bash
docker compose ps
```
![](Lab/EXPERIMENT 6/image-15.png)
---

#### Problem 2: Volume + Network Configuration

**Given Docker Run commands:**
```bash
docker network create app-net

docker run -d \
  --name postgres-db \
  --network app-net \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=secret \
  -v pgdata:/var/lib/postgresql/data \
  postgres:15

docker run -d \
  --name backend \
  --network app-net \
  -p 8000:8000 \
  -e DB_HOST=postgres-db \
  -e DB_USER=admin \
  -e DB_PASS=secret \
  python:3.11-slim
```
![](Lab/EXPERIMENT 6/image-16.png)
**Equivalent `docker-compose.yml`:**
```yaml
version: '3.8'
services:
  postgres-db:
    image: postgres:15
    container_name: postgres-db
    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: secret
    volumes:
      - pgdata:/var/lib/postgresql/data
    networks:
      - app-net

  backend:
    image: python:3.11-slim
    container_name: backend
    ports:
      - "8000:8000"
    environment:
      DB_HOST: postgres-db
      DB_USER: admin
      DB_PASS: secret
    depends_on:
      - postgres-db
    networks:
      - app-net

volumes:
  pgdata:

networks:
  app-net:
```

![](Lab/EXPERIMENT 6/image-14.png)
**Run:**
```bash
docker compose up -d
```

**Stop and remove:**
```bash
docker compose down -v
```

---

## 📊 Comparison: Docker Run vs Docker Compose

| Feature | Docker Run | Docker Compose |
|---|---|---|
| Approach | Imperative | Declarative |
| Configuration | Command line flags | YAML file |
| Multi-container support | Complex (manual) | Easy (`depends_on`) |
| Reusability | Low | High |
| Version control | Difficult | Easy (commit YAML) |
| Networking | Manual (`--network`) | Auto-created |
| Volumes | Manual (`-v`) | Defined in YAML |
| Scaling | Not supported | `--scale` flag |

---

##  Result

Successfully completed:
-  Nginx container using Docker Run — verified at `http://localhost:8081`
-  Nginx container using Docker Compose — verified at `http://localhost:8081`
- WordPress + MySQL using Docker Run — verified at `http://localhost:8082`
-  WordPress + MySQL using Docker Compose — verified at `http://localhost:8082`
-  Docker Run to Compose conversion (Problems 1 & 2)
- Resource limits conversion (Task 4)
-  Custom Dockerfile with Compose (Task 5)
-  Multi-stage Dockerfile with Compose (Task 6)

---

##  Viva Questions

**Q1. What is Docker Compose?**
Docker Compose is a tool used to define and run multi-container Docker applications using a YAML configuration file (`docker-compose.yml`).

**Q2. What is the difference between Docker Run and Docker Compose?**
Docker Run executes containers manually using CLI commands (imperative), while Docker Compose manages multiple containers using a declarative YAML configuration file.

**Q3. What does `depends_on` do?**
It ensures that one service starts before another. For example, WordPress waits for MySQL to start before launching.

**Q4. Why are Docker networks used?**
Docker networks allow containers to communicate with each other using container names as hostnames, without exposing ports to the host machine.

**Q5. What is the difference between `image:` and `build:` in Compose?**
`image:` pulls a prebuilt image from Docker Hub, while `build:` builds a custom image from a local Dockerfile.

**Q6. What does `docker compose down -v` do?**
It stops and removes containers, networks, AND named volumes defined in the Compose file.

---

##  Conclusion

Docker Compose provides a structured and efficient way to manage multi-container applications compared to `docker run`. It simplifies deployment, improves maintainability, enables version control of infrastructure, and allows easy scaling of services using a single declarative YAML file.

---

*Experiment 6 | Containerization and DevOps Lab | UPES Dehradun*



<div style='page-break-after: always;'></div>


# Lab Experiment 7: CI/CD Pipeline using Jenkins, GitHub and Docker Hub

**Name:** Sourabh Saini
**Subject:** Containerization and DevOps

---

## 1. Aim

To design and implement a complete CI/CD pipeline using Jenkins, integrating source code from GitHub, and building & pushing Docker images to Docker Hub.

---

## 2. Objectives

- Understand CI/CD workflow using Jenkins (GUI-based tool)
- Create a structured GitHub repository with application + Jenkinsfile
- Build Docker images from source code
- Securely store Docker Hub credentials in Jenkins
- Automate build & push process using webhook triggers
- Use same host (Docker) as Jenkins agent

---

## 3. Theory

### What is Jenkins?

Jenkins is a web-based GUI automation server used to:
- Build applications
- Test code
- Deploy software

It provides:
- Dashboard (browser-based UI)
- Plugin ecosystem (GitHub, Docker, etc.)
- Pipeline as Code using `Jenkinsfile`

### What is CI/CD?

**Continuous Integration (CI):** Code is automatically built and tested after each commit.

**Continuous Deployment (CD):** Built artifacts (Docker images) are automatically delivered/deployed.

### Workflow Overview

```
Developer → GitHub → Webhook → Jenkins → Build → Docker Hub
```

---

## 4. Prerequisites

- Docker & Docker Compose installed
- GitHub account
- Docker Hub account
- Basic Linux command knowledge

---

## 5. Part A: GitHub Repository Setup

### 5.1 Project Structure

```
my-app/
├── app.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
```

### 5.2 Application Code — `app.py`

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from CI/CD Pipeline!"

app.run(host="0.0.0.0", port=80)
```

### 5.3 `requirements.txt`

```
flask
```

### 5.4 Dockerfile

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["python", "app.py"]
```

### 5.5 Jenkinsfile

```groovy
pipeline {
    agent any
    environment {
        IMAGE_NAME = "your-dockerhub-username/myapp"
    }
    stages {
        stage('Clone Source') {
            steps {
                git 'https://github.com/your-username/my-app.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:latest .'
            }
        }
        stage('Login to Docker Hub') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-token', variable: 'DOCKER_TOKEN')]) {
                    sh 'echo $DOCKER_TOKEN | docker login -u your-dockerhub-username --password-stdin'
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                sh 'docker push $IMAGE_NAME:latest'
            }
        }
    }
}
```

---

## 6. Part B: Jenkins Setup using Docker

### 6.1 `docker-compose.yml`

```yaml
version: '3.8'

services:
  jenkins:
    image: jenkins/jenkins:lts
    container_name: jenkins
    restart: always
    ports:
      - "8080:8080"
      - "50000:50000"
    volumes:
      - jenkins_home:/var/jenkins_home
      - /var/run/docker.sock:/var/run/docker.sock
    user: root

volumes:
  jenkins_home:
```

### 6.2 Start Jenkins

```bash
docker-compose up -d
```

Access Jenkins at: `http://localhost:8080`

### 6.3 Unlock Jenkins

```bash
docker exec -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

### 6.4 Initial Setup

- Install suggested plugins
- Create admin user (`SourabhSaini`)

---

## 7. Part C: Jenkins Configuration

### 7.1 Add Docker Hub Credentials

Path: `Manage Jenkins → Credentials → Add Credentials`
- **Type:** Secret Text
- **ID:** `dockerhub-token`
- **Value:** Docker Hub Access Token

### 7.2 Create Pipeline Job

1. `New Item → Pipeline`
2. **Name:** `ci-cd-pipeline`
3. Configure:
   - Pipeline script from SCM
   - SCM: Git
   - Repo URL: your GitHub repo
   - Script Path: `Jenkinsfile`

---

## 8. Part D: GitHub Webhook Integration

### 8.1 Configure Webhook

In GitHub: `Settings → Webhooks → Add Webhook`
- **Payload URL:** `http://<your-server-ip>:8080/github-webhook/`
- **Events:** Push events

### 8.2 Exposing Jenkins via LocalTunnel

Since Jenkins runs locally, we used `localtunnel` to expose it publicly for GitHub webhook integration:

```bash
npm install -g localtunnel
npx localtunnel --port 8080
```

This generated a public URL (e.g., `https://green-donuts-nail.loca.lt`) which was used as the webhook payload URL.

---

## 9. Part E: Execution Flow

| Stage | Action |
|-------|--------|
| **Code Push** | Developer pushes code to GitHub |
| **Webhook Trigger** | GitHub sends event to Jenkins |
| **Clone** | Jenkins pulls latest code from GitHub |
| **Build** | Docker builds image using Dockerfile |
| **Auth** | Jenkins logs into Docker Hub using stored token |
| **Push** | Image pushed to Docker Hub |
| **Done** | Docker image available globally |

---

## 10. Role of Same Host Agent

Jenkins runs inside Docker with the Docker socket mounted:

```
/var/run/docker.sock
```

This allows Jenkins to directly control the host's Docker daemon — building and pushing images without needing a separate agent node.

A custom **Permanent Agent** node (`Sourabh node `) was also configured in Jenkins under `Manage Jenkins → Nodes → New Node` to demonstrate multi-node agent setup.

---

## 11. Observations

- Jenkins GUI significantly simplifies CI/CD pipeline management
- GitHub acts as both source repository and pipeline definition store (via `Jenkinsfile`)
- Docker ensures consistent, reproducible builds across environments
- Webhook integration enables fully automated, event-driven pipelines
- `localtunnel` provides a quick way to expose local Jenkins to the internet for webhook testing
- The Docker socket mount allows Jenkins to control the host Docker engine directly

---

## 12. Result

Successfully implemented a complete CI/CD pipeline where:
- Source code and pipeline definition are maintained in GitHub
- Jenkins automatically detects code changes via GitHub webhook
- Docker image is built on the host agent
- Image is securely pushed to Docker Hub using stored credentials

---

## 13. Screenshots

### Screenshot 1 — Jenkins Plugin Installation (Getting Started)
![](Lab/EXPERIMENT 7/image.png)

> Jenkins loading suggested plugins during the initial setup wizard at `localhost:8080`.

---

### Screenshot 2 — Create First Admin User
![](Lab/EXPERIMENT 7/image1.png)

> Creating the admin user `Sourabh Saini` during Jenkins initial configuration.

---

### Screenshot 3 — LocalTunnel Warning Page
![](Lab/EXPERIMENT 7/image2.png)

> The localtunnel gateway page for `https://green-donuts-nail.loca.lt` — requiring IP confirmation before accessing Jenkins publicly.

---

### Screenshot 4 — LocalTunnel Setup in Terminal
![](Lab/EXPERIMENT 7/image3.png)

> Terminal showing `npm install -g localtunnel`, `docker ps` confirming Jenkins container is running, and `npx localtunnel --port 8080` generating the public tunnel URL.

---

### Screenshot 5 — LocalTunnel Connection Error (Firewall)
![](Lab/EXPERIMENT 7/image4.png)

> Localtunnel connection refused error due to firewall settings — resolved by switching to `npx localtunnel` instead of the global `lt` command.

---

### Screenshot 6 — Jenkins Account Settings
![](Lab/EXPERIMENT 7/image5.png)

> Jenkins user account page for `sourabhsaini` showing profile, credentials, and email settings via the localtunnel public URL.

---

### Screenshot 7 — Adding New Node (Agent)
![](Lab/EXPERIMENT 7/image9.png)
> Creating a new Permanent Agent node named `Sourabh node` in Jenkins under `Manage Jenkins → Nodes → New Node`.

---

### Screenshot 8 — Nodes Dashboard
![](Lab/EXPERIMENT 7/image6.png)

> Jenkins Nodes page showing the `Built-In Node` (Linux aarch64) and the newly added `Sourabh node ` agent.

---

### Screenshot 9 — Agent Connection Command
![](Lab/EXPERIMENT 7/Screenshot 2026-04-01 at 9.15.44 AM.png)

> Jenkins displaying the JNLP agent connection commands (Unix/Windows) with a secret token to connect `Sourabh node ` as a remote agent.

---

## 14. Viva Questions

**Q1. What is the role of Jenkinsfile?**
It defines the CI/CD pipeline as code, stored in the repository alongside the application source.

**Q2. How does Jenkins integrate with GitHub?**
Through GitHub Webhooks — GitHub sends a POST request to Jenkins on every push event, triggering the pipeline automatically.

**Q3. Why is Docker used in CI/CD?**
Docker ensures consistent, reproducible builds across different environments by packaging the application and its dependencies into an image.

**Q4. What is a webhook?**
A webhook is an HTTP callback that allows GitHub to notify Jenkins of events (like a push) in real time.

**Q5. Why store Docker Hub token in Jenkins credentials?**
To avoid hardcoding secrets in the Jenkinsfile, which is stored in a public/shared repository. Jenkins credentials store is encrypted and secure.

**Q6. What is the benefit of using the same host as agent?**
Jenkins can directly invoke Docker commands on the host, eliminating the need for a separate build agent and simplifying the setup.

---

## 15. Key Takeaways

- Jenkins is GUI-based but pipelines are fully code-driven via `Jenkinsfile`
- Always use the credentials store — **never hardcode secrets**
- Webhooks make CI/CD fully automatic and event-driven
- Docker socket mounting (`/var/run/docker.sock`) allows Jenkins to act as its own Docker agent
- `localtunnel` is a quick solution for exposing local services during development/testing

---

*Experiment completed successfully on April 1, 2026.*



<div style='page-break-after: always;'></div>


# Experiment 8: Chef - Configuration Management

**Name:** Sourabh Saini
**Subject:** Containerization and DevOps

---

## Problem Statement

Managing infrastructure manually across multiple servers leads to configuration drift, inconsistent environments, and time-consuming repetitive tasks. While Ansible solves this with agentless SSH, Chef offers a pull-based approach where nodes regularly check in with a central server, ensuring continuous compliance even when network connections are intermittent.

---

## 1. What is Chef?

Chef is an automation platform that transforms infrastructure into code using **Ruby-based DSL** (Domain Specific Language). It follows a **pull-based model** where agents (Chef clients) periodically pull configurations from a central Chef server.

**Key Difference from Ansible:** Chef requires an agent on managed nodes and a central server, but offers more powerful dependency management and scales better for large enterprises.

---

## 2. How Chef Solves the Problem

- **Pull-based Model:** Nodes check in with Chef server regularly, ensuring consistent state
- **Idempotent Resources:** Resources ensure desired state regardless of how many times applied
- **Infrastructure as Code:** All configurations version-controlled and testable
- **Community Cookbooks:** Reusable configurations for common applications

---

## 3. Key Concepts

| Term | Description |
|------|-------------|
| **Chef Server** | Central repository for cookbooks, policies, and node data |
| **Chef Workstation** | Development machine where cookbooks are created and tested |
| **Chef Node** | Managed machine with Chef client installed |
| **Cookbook** | Collection of recipes, attributes, templates, and files |
| **Recipe** | Ruby-based file containing resource declarations |
| **Resource** | Building blocks (`package`, `service`, `file`, `template`, etc.) |
| **Run List** | Ordered list of recipes applied to a node |
| **Ohai** | System profiling tool that collects node attributes |

---

## 4. How Chef Works — Architecture

```
CHEF SERVER ARCHITECTURE
─────────────────────────────────────────────────────

  WORKSTATION              CHEF SERVER (Port 443)
  ┌──────────────┐         ┌──────────────────────┐
  │ • Cookbooks  │─────────▶ • Cookbooks (versioned)│
  │ • Roles      │  knife   │ • Node Data          │
  │ • Environments│  upload │ • Client Auth Keys   │
  │ • Data Bags  │         │ • Search Indexes      │
  └──────────────┘         └──────────────────────┘
                                      │
                              Pull (every 30 min)
                                      │
                           ┌──────────▼──────────┐
                           │    MANAGED NODES     │
                           │  Chef Client (Agent) │
                           │  Chef Client (Agent) │
                           └─────────────────────┘
```

---

## 5. Benefits of Chef

- **Pull-based Architecture:** Nodes check in regularly, ensuring compliance
- **Powerful Ruby DSL:** More expressive than YAML for complex logic
- **Large Community:** 4000+ community cookbooks
- **Test Kitchen:** Built-in testing framework
- **Compliance:** Continuous auditing capabilities

---

## Part A: Chef Solo (Simpler — No Server Required)

### Architecture

```
CHEF SOLO ARCHITECTURE
──────────────────────────────────────────────

  CONTROL NODE (Your Machine)    MANAGED NODES
  ┌─────────────────────┐        ┌───────────────────┐
  │ • Cookbooks         │──ssh──▶│ Chef Client       │
  │ • Recipes           │  scp   │ (Local Mode)      │
  │ • Attributes        │        └───────────────────┘
  │ • Templates         │
  └─────────────────────┘
  No central server needed — runs in local mode
```

---

### Step 1: Install Chef Workstation

```bash
# Ubuntu/Debian installation
wget https://packages.chef.io/files/stable/chef-workstation/24.10.1144/ubuntu/22.04/chef-workstation_24.10.1144-1_amd64.deb
sudo dpkg -i chef-workstation_24.10.1144-1_amd64.deb

# Verify installation
chef --version
# Expected: Chef Workstation version: 24.10.1144

# Install Chef Client on managed nodes (Docker containers)
docker exec server1 apt-get update
docker exec server1 apt-get install -y curl
docker exec server1 curl -L https://omnitruck.chef.io/install.sh | bash
```
![](Lab/EXPERIMENT 8/exp8%20screenshots/image.png)
---

### Step 2: Setup Lab Environment (Docker Containers)

```bash
# Create network
docker network create chef-lab

# Create SSH key pair
ssh-keygen -t rsa -b 4096 -f ~/.ssh/chef-key -N ""

# Build Chef-ready Docker image
cat > Dockerfile.chef << 'EOF'
FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y python3 openssh-server sudo curl systemd && \
    apt-get clean

RUN mkdir -p /var/run/sshd && \
    echo 'root:chef' | chpasswd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config

RUN mkdir -p /root/.ssh && chmod 700 /root/.ssh
COPY ~/.ssh/chef-key.pub /root/.ssh/authorized_keys
RUN chmod 600 /root/.ssh/authorized_keys

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
EOF

# Build image
docker build -f Dockerfile.chef -t chef-node .

# Create 4 test nodes
for i in {1..4}; do
  docker run -d \
    --name node${i} \
    --network chef-lab \
    -p 222${i}:22 \
    chef-node
  echo "Node${i} created with SSH on port 222${i}"
done

# Copy SSH key to nodes
for i in {1..4}; do
  docker exec node${i} mkdir -p /root/.ssh
  docker cp ~/.ssh/chef-key.pub node${i}:/root/.ssh/authorized_keys
  docker exec node${i} chmod 600 /root/.ssh/authorized_keys
done
```
![](Lab/EXPERIMENT 8/exp8%20screenshots/image-2.png)
![](Lab/EXPERIMENT 8/exp8%20screenshots/image-1.png)
![](Lab/EXPERIMENT 8/exp8%20screenshots/image-3.png)
---

### Step 3: Create First Cookbook

```bash
mkdir -p ~/chef-repo/cookbooks
cd ~/chef-repo

chef generate cookbook cookbooks/basics

cat > cookbooks/basics/metadata.rb << 'EOF'
name 'basics'
maintainer 'DevOps Lab'
maintainer_email 'lab@example.com'
license 'Apache-2.0'
description 'Installs/Configures basic system settings'
version '0.1.0'
chef_version '>= 16.0'
depends 'apt'
EOF
```
![](Lab/EXPERIMENT 8/exp8%20screenshots/image-4.png)
---

### Step 4: Create Recipes

**Default Recipe** — `cookbooks/basics/recipes/default.rb`

```ruby
include_recipe 'basics::packages'
include_recipe 'basics::files'
include_recipe 'basics::services'
```
![](Lab/EXPERIMENT 8/exp8%20screenshots/image-6.png)
**Packages Recipe** — `cookbooks/basics/recipes/packages.rb`

```ruby
apt_update 'update' do
  action :update
  frequency 86400
end

%w(vim htop wget curl git net-tools).each do |pkg|
  package pkg do
    action :install
  end
end

package 'python3' do
  action :install
  version '3.10.*'
end
```
![](Lab/EXPERIMENT 8/exp8%20screenshots/image-7.png)
**Files Recipe** — `cookbooks/basics/recipes/files.rb`

```ruby
directory '/opt/chef-demo' do
  owner 'root'
  group 'root'
  mode '0755'
  action :create
end

file '/opt/chef-demo/README.md' do
  content <<~EOH
    # Chef Managed System
    ======================
    Hostname: #{node['hostname']}
    IP Address: #{node['ipaddress']}
    OS: #{node['platform']} #{node['platform_version']}
    Managed by: Chef
    Last Converged: #{Time.now}
  EOH
  mode '0644'
  action :create
end

cookbook_file '/opt/chef-demo/welcome.txt' do
  source 'welcome.txt'
  mode '0644'
  action :create
end
```

**Services Recipe** — `cookbooks/basics/recipes/services.rb`

```ruby
service 'ssh' do
  action [:enable, :start]
end

template '/etc/systemd/system/demo.service' do
  source 'demo.service.erb'
  owner 'root'
  group 'root'
  mode '0644'
  notifies :run, 'execute[systemctl daemon-reload]', :immediately
end

execute 'systemctl daemon-reload' do
  command 'systemctl daemon-reload'
  action :nothing
end

service 'demo' do
  action [:enable, :start]
  subscribes :restart, 'template[/etc/systemd/system/demo.service]'
end
```

---

### Step 5: Create Templates and Files

**Service Template** — `cookbooks/basics/templates/demo.service.erb`

```ini
[Unit]
Description=Chef Demo Service
After=network.target

[Service]
Type=simple
ExecStart=/bin/bash -c 'while true; do echo "Chef Demo Service: $(date)" >> /var/log/demo.log; sleep 60; done'
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```
![](Lab/EXPERIMENT 8/exp8%20screenshots/image-8.png)
**Welcome File** — `cookbooks/basics/files/welcome.txt`

```
=====================================
Welcome to Chef Managed System
=====================================
This system is configured using Chef.
All changes should be made through cookbooks.
=====================================
```

---

### Step 6: Create Node Inventory

```bash
cat > nodes.json << 'EOF'
{
  "node1": { "run_list": ["recipe[basics]"] },
  "node2": { "run_list": ["recipe[basics]"] },
  "node3": { "run_list": ["recipe[basics]"] },
  "node4": { "run_list": ["recipe[basics]"] }
}
EOF

mkdir -p ~/chef-repo/.chef
cat > ~/chef-repo/.chef/config.rb << 'EOF'
current_dir = File.dirname(__FILE__)
node_name 'workstation'
client_key "#{current_dir}/workstation.pem"
chef_repo_path "#{current_dir}/.."
cookbook_path ["#{current_dir}/../cookbooks"]
EOF

cat > ~/chef-repo/run-chef.sh << 'EOF'
#!/bin/bash
for i in {1..4}; do
  echo "====================================="
  echo "Configuring node${i}"
  echo "====================================="
  ssh -i ~/.ssh/chef-key -o StrictHostKeyChecking=no root@localhost -p 222${i} "mkdir -p /opt/chef/cookbooks"
  scp -i ~/.ssh/chef-key -P 222${i} -r ~/chef-repo/cookbooks root@localhost:/opt/chef/
  ssh -i ~/.ssh/chef-key -p 222${i} root@localhost << 'ENDSSH'
cd /opt/chef
chef-client --local-mode --runlist 'recipe[basics]'
ENDSSH
  echo "Node${i} configured successfully"
done
EOF
chmod +x ~/chef-repo/run-chef.sh
```

---

### Step 7: Run Chef Solo

```bash
cd ~/chef-repo
./run-chef.sh

# Verify changes on nodes
for i in {1..4}; do
  echo "=== Node${i} ==="
  ssh -i ~/.ssh/chef-key -p 222${i} root@localhost "cat /opt/chef-demo/README.md"
  echo ""
done
```
![](Lab/EXPERIMENT 8/exp8%20screenshots/image-9.png)
---

## Part B: Chef Server (Full Enterprise Setup)

### Step 1: Setup Chef Server

```bash
docker pull chef/chef-server:latest

docker run -d \
  --name chef-server \
  --network chef-lab \
  -p 443:443 \
  -v chef-server-data:/var/opt/opscode \
  chef/chef-server:latest

docker logs -f chef-server

docker exec chef-server chef-server-ctl user-create \
  admin "Admin" "User" admin@example.com 'admin123' \
  --filename /tmp/admin.pem

docker exec chef-server chef-server-ctl org-create \
  devops "DevOps Lab" --association admin \
  --filename /tmp/devops-validator.pem

docker cp chef-server:/tmp/admin.pem ~/chef-repo/.chef/
docker cp chef-server:/tmp/devops-validator.pem ~/chef-repo/.chef/
```

---
![](Lab/EXPERIMENT 8/image.png)

### Step 2: Configure Knife

```bash
cat > ~/chef-repo/.chef/knife.rb << 'EOF'
current_dir = File.dirname(__FILE__)
log_level :info
log_location STDOUT
node_name "admin"
client_key "#{current_dir}/admin.pem"
validation_client_name "devops-validator"
validation_key "#{current_dir}/devops-validator.pem"
chef_server_url "https://chef-server/organizations/devops"
cookbook_path ["#{current_dir}/../cookbooks"]
ssl_verify_mode :verify_none
EOF

cd ~/chef-repo
knife ssl check
knife client list
```

---
![](Lab/EXPERIMENT 8/image-1.png)

### Step 3: Create Advanced Cookbook (webapp)

```bash
chef generate cookbook cookbooks/webapp
```

**Default Recipe**

```ruby
include_recipe 'webapp::webserver'
include_recipe 'webapp::app'
```

**Webserver Recipe**

```ruby
package 'nginx' do
  action :install
end

template '/etc/nginx/sites-available/webapp' do
  source 'webapp.conf.erb'
  owner 'root'
  group 'root'
  mode '0644'
  notifies :reload, 'service[nginx]'
end

link '/etc/nginx/sites-enabled/webapp' do
  to '/etc/nginx/sites-available/webapp'
  notifies :reload, 'service[nginx]'
end

file '/etc/nginx/sites-enabled/default' do
  action :delete
  notifies :reload, 'service[nginx]'
end

service 'nginx' do
  action [:enable, :start]
end
```
![](Lab/EXPERIMENT 8/image-2.png)
**App Recipe**

```ruby
apt_repository 'nodejs' do
  uri 'https://deb.nodesource.com/node_16.x'
  components ['main']
  key 'https://deb.nodesource.com/gpgkey/nodesource.gpg.key'
  action :add
end

package 'nodejs' do
  action :install
end

directory '/opt/webapp' do
  owner 'root'
  group 'root'
  mode '0755'
  action :create
end

git '/opt/webapp' do
  repository 'https://github.com/chef-training/sample-node-app.git'
  revision 'main'
  action :sync
  notifies :run, 'execute[npm install]', :immediately
end

execute 'npm install' do
  cwd '/opt/webapp'
  command 'npm install --production'
  action :nothing
end

template '/etc/systemd/system/webapp.service' do
  source 'webapp.service.erb'
  owner 'root'
  group 'root'
  mode '0644'
  notifies :run, 'execute[systemctl daemon-reload]', :immediately
  notifies :restart, 'service[webapp]'
end

execute 'systemctl daemon-reload' do
  command 'systemctl daemon-reload'
  action :nothing
end

service 'webapp' do
  action [:enable, :start]
end
```

---
![](Lab/EXPERIMENT 8/image-3.png)
### Step 4: Create Templates

**Nginx Config** — `cookbooks/webapp/templates/webapp.conf.erb`

```nginx
server {
    listen 80;
    server_name <%= node['hostname'] %>;

    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```
![](Lab/EXPERIMENT 8/image-4.png)
**Webapp Service** — `cookbooks/webapp/templates/webapp.service.erb`

```ini
[Unit]
Description=Node.js Web Application
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/opt/webapp
ExecStart=/usr/bin/node server.js
Restart=on-failure
Environment=NODE_ENV=production
Environment=PORT=3000

[Install]
WantedBy=multi-user.target
```

---

### Step 5: Bootstrap Nodes

```bash
for i in {1..4}; do
  docker exec node${i} curl -L https://omnitruck.chef.io/install.sh | bash
  docker cp ~/chef-repo/.chef/devops-validator.pem node${i}:/etc/chef/
  docker exec node${i} bash -c "cat > /etc/chef/client.rb << 'EOF'
log_level :info
log_location STDOUT
chef_server_url 'https://chef-server/organizations/devops'
validation_client_name 'devops-validator'
validation_key '/etc/chef/devops-validator.pem'
node_name 'node${i}'
ssl_verify_mode :verify_none
EOF"
done
```

---

### Step 6: Upload Cookbook and Bootstrap

```bash
cd ~/chef-repo
knife cookbook upload webapp

for i in {1..4}; do
  knife bootstrap localhost \
    --ssh-user root \
    --ssh-port 222${i} \
    --ssh-identity-file ~/.ssh/chef-key \
    --node-name node${i} \
    --run-list 'recipe[webapp]'
done

knife node list
knife status
```

---

### Step 7: Verify Configuration

```bash
knife node show node1
knife search node "platform:ubuntu"

knife ssh "name:node1" "chef-client" \
  --ssh-user root \
  --ssh-identity-file ~/.ssh/chef-key \
  --attribute ipaddress

for i in {1..4}; do
  echo "=== Node${i} ==="
  curl -s http://localhost:222${i} || echo "Service not accessible"
done
```

---
![](Lab/EXPERIMENT 8/image-6.png)
![](Lab/EXPERIMENT 8/image-7.png)

## 6. Comparison: Chef Solo vs Chef Server

| Aspect | Chef Solo (Part A) | Chef Server (Part B) |
|--------|-------------------|---------------------|
| Complexity | Low | High |
| Setup Time | ~15 minutes | ~45 minutes |
| Server Required | No | Yes |
| Scalability | Manual per node | Centralized |
| Node Management | Direct SSH | Chef Server |
| Search Capabilities | No | Yes |
| Role-Based Config | Limited | Full support |
| Best For | Learning, small setups | Production, enterprises |

---

## 7. Chef vs Ansible Comparison

| Feature | Chef | Ansible |
|---------|------|---------|
| Architecture | Pull-based (agent) | Push-based (agentless) |
| Language | Ruby DSL | YAML |
| Learning Curve | Steep | Gentle |
| Setup Complexity | High | Low |
| Idempotency | Yes | Yes |
| Real-time Changes | Delayed (pull interval) | Immediate (push) |
| Scaling | Excellent (5000+ nodes) | Good (up to 2000 nodes) |
| Community | Mature, 4000+ cookbooks | Largest, 3000+ collections |
| Use Case | Large enterprises | Small to medium, cloud |


---

## 9. Cleanup

```bash
for i in {1..4}; do docker rm -f node${i}; done
docker rm -f chef-server
rm -rf ~/chef-repo
```

---

## 10. Optional Read — Chef Solo vs Ansible Deep Dive

### What was Chef Solo?

Chef Solo allowed running Chef **without a central server**. It ran locally on a machine, with cookbooks and JSON configs provided manually — essentially *"a script executor with idempotency"*.

**Key limitations:**
- No centralized state management
- No node discovery or inventory management
- No orchestration across nodes
- No API or UI

### Core Conceptual Difference

| | Chef Solo | Ansible |
|--|-----------|---------|
| Agent required | No | No |
| Central control | No | Yes |
| Multi-node orchestration | No | Yes |
| Config delivery | Manual copy per machine | Push from control node |
| Node awareness | None | Global inventory view |

### Why Chef Solo Never Became Dominant

It lacked what modern DevOps needed — infrastructure orchestration, central visibility, easy scaling, and simplicity. Ansible solved all of these without requiring agents.

### Evolution Timeline

```
Chef (classic)  →  Heavy, enterprise, agent-based
Chef Solo       →  Lightweight but very limited
Ansible         →  Agentless + centralized (sweet spot)
```

### Simple Analogy

- **Chef with server:** Manager giving instructions via a central system
- **Chef Solo:** Giving each worker a USB stick with instructions
- **Ansible:** A remote control system managing all workers live

---

## 11. Observations

- Chef uses a **pull-based model** — nodes periodically converge to desired state
- **Idempotency** is core — running the same recipe multiple times produces the same result
- Chef Solo is ideal for learning; Chef Server is production-grade and enterprise-ready
- `knife` is the primary CLI for interacting with Chef Server
- Recipes written in Ruby DSL are more powerful but steeper to learn than Ansible's YAML
- Docker-based lab setup simplifies node provisioning for learning purposes

---

## 12. Result

Successfully studied and implemented Chef configuration management:
- **Part A (Chef Solo):** Local mode cookbook execution across Docker nodes via SSH
- **Part B (Chef Server):** Full enterprise setup with `knife` bootstrapping and centralized cookbook management
- Compared Chef Solo vs Chef Server and Chef vs Ansible in terms of architecture, scalability, and use cases

---

## 13. Viva Questions

**Q1. What is the difference between Chef Solo and Chef Server?**
Chef Solo runs locally without a central server — cookbooks are manually pushed to nodes. Chef Server provides centralized management where nodes pull their configurations automatically every ~30 minutes.

**Q2. What is a Cookbook in Chef?**
A Cookbook is the fundamental unit of configuration — it contains recipes, attributes, templates, files, and metadata defining how a node should be configured.

**Q3. What is idempotency in Chef?**
Idempotency means applying a recipe multiple times always results in the same system state. Chef resources only make changes when the current state differs from the desired state.

**Q4. What is `knife` in Chef?**
`knife` is the CLI tool used to interact with the Chef Server — uploading cookbooks, bootstrapping nodes, running remote commands, and querying node data.

**Q5. What is Ohai?**
Ohai is Chef's system discovery tool that automatically collects node attributes (hostname, IP, OS, memory, etc.) and makes them available in recipes as `node['attribute']`.

**Q6. Why is Chef pull-based while Ansible is push-based?**
In Chef, the Chef client on each node periodically contacts the Chef Server and pulls its configuration. In Ansible, the control node pushes commands to managed nodes via SSH — no agent is needed.

**Q7. What is a Run List?**
A Run List is an ordered list of recipes and roles assigned to a node, defining what configurations will be applied during a Chef client run.

---

## 14. Key Takeaways

- Chef transforms infrastructure into code using **Ruby DSL**
- **Pull-based model** ensures nodes continuously converge to desired state
- Chef Solo = no server, manual delivery; Chef Server = centralized, scalable
- Ansible is simpler and agentless — better for small/medium environments
- Chef excels in **large enterprises** needing complex dependency management
- Always use Chef's credentials mechanisms — **never hardcode secrets** in recipes

---

## 15. References

- Official Website: [https://www.chef.io](https://www.chef.io)
- Documentation: [https://docs.chef.io](https://docs.chef.io)
- Chef Supermarket: [https://supermarket.chef.io](https://supermarket.chef.io)
- Learn Chef: [https://learn.chef.io](https://learn.chef.io)

---

*Experiment completed as part of Containerization and DevOps Lab.*



<div style='page-break-after: always;'></div>


# Experiment 9 — Ansible: Configuration Management and Automation

## Theory

### Problem Statement

Managing infrastructure manually across multiple servers leads to configuration drift, inconsistent environments, and time-consuming repetitive tasks. Scaling from one server to hundreds becomes nearly impossible with manual SSH-based administration.

### What is Ansible?

Ansible is an open-source automation tool for **configuration management**, **application deployment**, and **orchestration**. It follows an **agentless architecture** — using SSH for Linux and WinRM for Windows — and uses YAML-based **playbooks** to define automation tasks.

Ansible has become the standard choice among enterprise automation solutions because it is simple yet powerful, agentless, community-powered, predictable, and secure.

### How Ansible Solves the Problem

| Problem | Ansible Solution |
|---|---|
| Agent installation on every server | Agentless — uses SSH only |
| Running playbooks twice breaks things | Idempotency — same result every time |
| Imperative scripts hard to read | Declarative YAML — describe desired state |
| Waiting for changes to propagate | Push-based — initiates from control node immediately |

---

## Key Concepts

| Component | Description |
|---|---|
| **Control Node** | Machine with Ansible installed — where you run commands |
| **Managed Nodes** | Target servers — no Ansible agent needed |
| **Inventory** | File listing all managed nodes (EC2 instances, servers, etc.) |
| **Playbooks** | YAML files containing a sequence of automation steps |
| **Tasks** | Individual actions in playbooks (e.g., installing a package) |
| **Modules** | Built-in functionality to perform tasks (e.g., `apt`, `yum`, `service`) |
| **Roles** | Pre-defined reusable automation scripts |

### How Ansible Works

Ansible connects from the **control node** to the **managed nodes** via SSH, sending commands and instructions. The units of code it executes are called **modules**. Each module is invoked by a **task**, and an ordered list of tasks forms a **playbook**. The managed machines are listed in an **inventory file** grouped into categories.

```
Control Node (Ansible installed)
        │
        │ SSH
        ├──────────── Managed Node 1
        ├──────────── Managed Node 2
        └──────────── Managed Node 3
```

No extra agents required on managed nodes — just a terminal and a text editor to get started.

---

## Part A — Hands-On Lab

### Step 1: Install Ansible

**Via pip (recommended for macOS/Linux):**

```bash
pip install ansible
ansible --version
```

**Via apt (Ubuntu/Debian):**

```bash
sudo apt update -y
sudo apt install ansible -y
ansible --version
```

**Post-installation check:**

```bash
ansible localhost -m ping
```

**Expected output:**

```
localhost | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```

---

### Step 2: Create SSH Key Pair

Ansible uses SSH key-based authentication to connect to managed nodes without passwords.

```bash
ssh-keygen -t rsa -b 4096
# Accept all defaults — keys saved to ~/.ssh/id_rsa and ~/.ssh/id_rsa.pub
```

Copy keys to the current working directory (needed for building the Docker image):

```bash
cp ~/.ssh/id_rsa.pub .
cp ~/.ssh/id_rsa .
```

**Key placement explained:**

| File | Location | Purpose |
|---|---|---|
| `id_rsa` (Private Key) | Control node only | Used to authenticate when connecting — **never share this** |
| `id_rsa.pub` (Public Key) | Remote server `~/.ssh/authorized_keys` | Grants access to anyone with the matching private key |

---

### Step 3: Create the Docker Image (Ubuntu SSH Server)

Create a `Dockerfile` that builds a custom Ubuntu image with OpenSSH pre-configured and our public key baked in:

```dockerfile
FROM ubuntu

RUN apt update -y
RUN apt install -y python3 python3-pip openssh-server
RUN mkdir -p /var/run/sshd

# Configure SSH
RUN mkdir -p /run/sshd && \
    echo 'root:password' | chpasswd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config && \
    sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/' /etc/ssh/sshd_config

# Create .ssh directory and set proper permissions
RUN mkdir -p /root/.ssh && \
    chmod 700 /root/.ssh

# Copy SSH keys into the image
COPY id_rsa /root/.ssh/id_rsa
COPY id_rsa.pub /root/.ssh/authorized_keys

# Set proper permissions
RUN chmod 600 /root/.ssh/id_rsa && \
    chmod 644 /root/.ssh/authorized_keys

# Fix for SSH login
RUN sed -i 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' /etc/pam.d/sshd

# Expose SSH port
EXPOSE 22

# Start SSH service
CMD ["/usr/sbin/sshd", "-D"]
```

Build the image:

```bash
docker build -t ubuntu-server .
```

---
![](Lab/EXPERIMENT 9/image.png)
### Step 4: Launch 4 Server Containers

```bash
for i in {1..4}; do
    echo -e "\n Creating server${i}\n"
    docker run -d --rm -p 220${i}:22 --name server${i} ubuntu-server
    echo -e "IP of server${i} is $(docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' server${i})"
done
```

**Expected output:**

```
Creating server1
IP of server1 is 172.17.0.2

Creating server2
IP of server2 is 172.17.0.3

Creating server3
IP of server3 is 172.17.0.4

Creating server4
IP of server4 is 172.17.0.5
```

---

### Step 5: Create Ansible Inventory

This script auto-generates `inventory.ini` with the real container IPs:

```bash
echo "[servers]" > inventory.ini
for i in {1..4}; do
    docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' server${i} >> inventory.ini
done

cat << EOF >> inventory.ini

[servers:vars]
ansible_user=root
ansible_ssh_private_key_file=~/.ssh/id_rsa
ansible_python_interpreter=/usr/bin/python3
EOF
```

Review the generated file:

```bash
cat inventory.ini
```

**Expected `inventory.ini` content:**

![](Lab/EXPERIMENT 9/image-2.png)

### Step 6: Test Connectivity

Manual SSH test to confirm keys work:

```bash
ssh -i ~/.ssh/id_rsa root@172.17.0.2
```

Ansible ping test across all servers:

```bash
ansible all -i inventory.ini -m ping
```

**Expected output:**

```
172.17.0.2 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
172.17.0.3 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
172.17.0.4 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
172.17.0.5 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```
![](Lab/EXPERIMENT 9/image-3.png)
For verbose output (useful for debugging):





### Step 7: Create and Run Playbook (`update.yml`)


```yaml
---
- name: Update and configure servers
  hosts: all
  become: yes
  tasks:

    - name: Update apt packages
      apt:
        update_cache: yes
        upgrade: dist

    - name: Install required packages
      apt:
        name: ["vim", "htop", "wget"]
        state: present

    - name: Create test file
      copy:
        dest: /root/ansible_test.txt
        content: "Configured by Ansible on {{ inventory_hostname }}"
```
![](Lab/EXPERIMENT 9/image4.png)
Run the playbook:

```bash
ansible-playbook -i inventory.ini update.yml
```

**Expected output:**

```
PLAY [Update and configure servers] ********************************************

TASK [Gathering Facts] *********************************************************
ok: [172.17.0.2]
ok: [172.17.0.3]
ok: [172.17.0.4]
ok: [172.17.0.5]

TASK [Update apt packages] *****************************************************
changed: [172.17.0.2]
changed: [172.17.0.3]
...

TASK [Install required packages] ***********************************************
changed: [172.17.0.2]
...

TASK [Create test file] ********************************************************
changed: [172.17.0.2]
...

PLAY RECAP *********************************************************************
172.17.0.2  : ok=4  changed=3  unreachable=0  failed=0
172.17.0.3  : ok=4  changed=3  unreachable=0  failed=0
172.17.0.4  : ok=4  changed=3  unreachable=0  failed=0
172.17.0.5  : ok=4  changed=3  unreachable=0  failed=0
```

---
![](Lab/EXPERIMENT 9/image11.png)

### Step 8: Create Advanced Playbook (`playbook1.yml`)

```yaml
---
- name: Configure multiple servers
  hosts: servers
  become: yes
  tasks:

    - name: Update apt package index
      apt:
        update_cache: yes

    - name: Install Python 3 (latest available)
      apt:
        name: python3
        state: latest

    - name: Create test file with content
      copy:
        dest: /root/test_file.txt
        content: |
          This is a test file created by Ansible
          Server name: {{ inventory_hostname }}
          Current date: {{ ansible_date_time.date }}

    - name: Display system information
      command: uname -a
      register: uname_output

    - name: Show disk space
      command: df -h
      register: disk_space

    - name: Print results
      debug:
        msg:
          - "System info: {{ uname_output.stdout }}"
          - "Disk space: {{ disk_space.stdout_lines }}"
```

Run it:

```bash
ansible-playbook -i inventory.ini playbook1.yml
```

---

### Step 9: Verify Changes

Using Ansible to read the created file across all servers:

```bash
ansible all -i inventory.ini -m command -a "cat /root/ansible_test.txt"
```
![](Lab/EXPERIMENT 9/image11.png)
Using Docker exec directly:

```bash
for i in {1..4}; do
    docker exec server${i} cat /root/ansible_test.txt
done
```
![](Lab/EXPERIMENT 9/lastimage.png)
**Expected output on each server:**

```
Configured by Ansible on 172.17.0.2
Configured by Ansible on 172.17.0.3
Configured by Ansible on 172.17.0.4
Configured by Ansible on 172.17.0.5
```

---


### Step 10: Cleanup

Stop all server containers:

```bash
for i in {1..4}; do
    docker rm -f server${i}
done
```

---



## Complete Workflow Summary

```
1. Setup SSH keys
        ↓
2. Build ubuntu-server Docker image
        ↓
3. Launch 4 containers (server1–server4)
        ↓
4. Generate inventory.ini with container IPs
        ↓
5. Test connectivity (ansible -m ping)
        ↓
6. Run playbook (ansible-playbook)
        ↓
7. Verify changes
        ↓
8. Cleanup (docker rm -f)
```

---

## Key Takeaways

1. **Agentless** — Ansible only needs SSH on managed nodes, no extra software to install
2. **Idempotent** — running the same playbook twice produces the same result, no unintended side effects
3. **Declarative** — you describe *what* you want (nginx installed, file present), not *how* to do it step by step
4. **Inventory** — the single source of truth for all managed nodes, supports groups and variables
5. **Modules** — 3000+ built-in modules cover everything from `apt`/`yum` to AWS/Azure/GCP resources
6. **`register` + `debug`** — capture command output and print it back, useful for auditing and troubleshooting
7. **Playbooks scale** — the same playbook that ran on 4 Docker containers runs identically on 400 EC2 instances

---

## Screenshots

>  All screenshots are stored in the `screenshots/` folder.


## References

- [Ansible Official Documentation](https://docs.ansible.com/)
- [Ansible Tutorial — Spacelift](https://spacelift.io/blog/ansible-tutorial)
- [Ansible Official Website](https://www.ansible.com/)
- [Ansible Tower GUI](https://ansible.github.io/lightbulb/decks/intro-to-ansible-tower.html)
- [Ansible Tower Tutorial — GeeksforGeeks](https://www.geeksforgeeks.org/devops/ansible-tower/)

---

*Experiment 9 | Containerization and DevOps Lab | UPES Dehradun*



<div style='page-break-after: always;'></div>


# Experiment 10: SonarQube — Static Code Analysis

**Name:** Sourabh Saini
**Roll No:** R2142230968
**Course:** Containerization and DevOps

---

## Objective

Perform static code analysis on a Java application using SonarQube to automatically detect bugs, security vulnerabilities, and code smells — and understand how it integrates into a CI/CD pipeline.

---

## Theory

### Problem Statement
Code bugs and security issues are often found too late — during testing or even after deployment. Manual code reviews are slow, inconsistent, and don't scale as teams grow.

### What is SonarQube?
SonarQube is an open-source platform that automatically scans source code for bugs, security vulnerabilities, and maintainability issues — **without running the code**. This is called **static analysis**.

### Key Terms

| Term | Meaning |
|------|---------|
| **Quality Gate** | A set of rules; code must pass before deployment |
| **Bug** | Code that will likely break or behave incorrectly |
| **Vulnerability** | A security weakness in the code |
| **Code Smell** | Code that works but is poorly written or hard to maintain |
| **Technical Debt** | Estimated time to fix all issues |
| **Coverage** | Percentage of code tested by unit tests |
| **Duplication** | Repeated code blocks (copy-paste) |

### Lab Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Your Machine / CI                    │
│                                                         │
│   ┌──────────────┐        ┌──────────────────────────┐  │
│   │  Your Code   │──────▶ │    Sonar Scanner         │  │
│   │  (Java, JS,  │ scans  │  (CLI / Maven / Jenkins) │  │
│   │   Python...) │        └────────────┬─────────────┘  │
│   └──────────────┘                     │ sends report   │
│                                        ▼                │
│                          ┌─────────────────────────┐    │
│                          │   SonarQube Server      │    │
│                          │   (runs on port 9000)   │    │
│                          │   ┌─────────────────┐   │    │
│                          │   │ Analysis Engine │   │    │
│                          │   │ Quality Gates   │   │    │
│                          │   │ Web Dashboard   │   │    │
│                          │   └────────┬────────┘   │    │
│                          └───────────┼─────────────┘    │
│                                      │ stores results   │
│                          ┌───────────▼─────────────┐    │
│                          │   PostgreSQL Database   │    │
│                          └─────────────────────────┘    │
└─────────────────────────────────────────────────────────┘
```

---

## Prerequisites

- Docker Desktop installed and running
- Maven (`mvn`) installed (or use the Docker-based scanner)
- Terminal / command line

Check Docker is running:

```bash
docker --version
docker-compose --version
```

---

## Step 1: Start the SonarQube Server

Navigate to the experiment folder and start all containers:

```bash
cd ~/Desktop/exp10
docker-compose up -d
```
![](Lab/EXPERIMENT 10/image.png)
Watch logs until you see **"SonarQube is operational"**:

```bash
docker-compose logs -f sonarqube
```

![](Lab/EXPERIMENT 10/image-1.png)



Verify containers are running:

```bash
docker ps
```
![](Lab/EXPERIMENT 10/image-2.png)
**Expected:** Two containers — `sonarqube` and `sonar-db` — both with status `Up`.


---

## Step 2: Open SonarQube Dashboard

Open your browser and go to:

```
http://localhost:9000
```

- Default credentials: **admin / admin**
- You will be prompted to change the password on first login (set it to something like `admin123`)

![](Lab/EXPERIMENT 10/image-3.png)

![](Lab/EXPERIMENT 10/image-4.png)

---

## Step 3: Generate an Authentication Token

The scanner needs a token to authenticate with the server.

1. Click your **user icon** (top right) → **My Account**
2. Click the **"Security"** tab
3. Under **"Generate Tokens"**, type a name: `scanner-token`
4. Click **"Generate"**
5. **Copy the token immediately** — it is shown only once!



![](Lab/EXPERIMENT 10/image-5.png)

Now export the token as an environment variable in your terminal (replace with your actual token):

```bash
export SONAR_TOKEN=sqp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## Step 4: Create the Sample Java Application

The project files are already created under `sample-java-app/`. Here is what each file contains:

### `src/main/java/com/example/Calculator.java`

A Java class intentionally containing:
- **Bug:** Division by zero (unhandled)
- **Code Smell:** Unused variable
- **Vulnerability:** SQL Injection risk
- **Code Smell:** Duplicated `multiply()` and `multiplyAlt()` methods
- **Bug:** Null pointer risk in `getName()`
- **Code Smell:** Empty catch block in `riskyOperation()`

### `pom.xml`

Maven build file with the SonarQube Maven plugin (`sonar-maven-plugin 3.9.1.2184`) configured.

---

## Step 5: Update the Token in pom.xml

Replace `YOUR_TOKEN_HERE` in `pom.xml` with your actual token:

```bash
cd ~/Desktop/exp10/sample-java-app
sed -i '' "s/YOUR_TOKEN_HERE/$SONAR_TOKEN/" pom.xml
```
![](Lab/EXPERIMENT 10/3.png)
Verify the replacement:

```bash
grep "sonar.login" pom.xml
```

---

## Step 6: Run the SonarQube Scan

### Option A — Maven Plugin (Recommended if Maven is installed)

```bash
cd ~/Desktop/exp10/sample-java-app
mvn sonar:sonar -Dsonar.login=$SONAR_TOKEN
```

Maven will compile the code and send the analysis report to the SonarQube server.



### Option B — Docker-based Scanner CLI (No Maven needed)

First, find the exact Docker network name:

```bash
docker network ls | grep sonarqube
```

Then run the scanner container:

```bash
cd ~/Desktop/exp10/sample-java-app

docker run --rm \
  --network exp10_sonarqube-lab \
  -e SONAR_TOKEN="$SONAR_TOKEN" \
  -v "$(pwd):/usr/src" \
  sonarsource/sonar-scanner-cli \
  -Dsonar.host.url=http://sonarqube:9000 \
  -Dsonar.projectBaseDir=/usr/src \
  -Dsonar.projectKey=sample-java-app
```

> **Note:** Use `http://sonarqube:9000` (container name), **not** `localhost`, because the scanner container is on the same Docker network as the server.

![](Lab/EXPERIMENT 10/step6.png)

---

## Step 7: View Results in the Dashboard

After the scan finishes, open:

```
http://localhost:9000/dashboard?id=sample-java-app
```

![](Lab/EXPERIMENT 10/dashboard.png)



---

## Step 8: Jenkins Integration (CI/CD — Reference)

Once SonarQube is working locally, it can be added to a Jenkins pipeline so every code commit is automatically scanned.

```groovy
// Jenkinsfile
pipeline {
    agent any
    environment {
        SONAR_HOST_URL = 'http://sonarqube:9000'
        SONAR_TOKEN = credentials('sonar-token')
    }
    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh 'mvn clean verify sonar:sonar'
                }
            }
        }
        stage('Quality Gate') {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
        stage('Build') {
            steps { sh 'mvn package' }
        }
        stage('Deploy') {
            steps {
                sh 'docker build -t sample-app .'
                sh 'docker run -d -p 8080:8080 sample-app'
            }
        }
    }
}
```
![](Lab/EXPERIMENT 10/jenkins.png)
![](Lab/EXPERIMENT 10/jenkins1.png)
![](Lab/EXPERIMENT 10/image-6.png)
**Pipeline flow:**

![](Lab/EXPERIMENT 10/image-7.png)
---



## Tool Comparison Matrix

| Feature | Jenkins | Ansible | Chef | SonarQube |
|---------|---------|---------|------|-----------|
| Primary Purpose | CI/CD Automation | Config Management | Config Management | Code Quality |
| Architecture | Master-Agent | Agentless | Client-Server | Client-Server |
| Language | Java / Groovy | YAML | Ruby | Java |
| Learning Curve | Moderate | Low | High | Low |
| Setup Complexity | Moderate | Simple | Complex | Simple |

---

## Key Concepts Summary

- **SonarQube Server** = The brain — receives, stores, and displays analysis results
- **Sonar Scanner** = The worker — reads your code and sends the report to the server
- **Both are required.** The Scanner needs a Token to talk to the Server
- **Quality Gates** automatically block bad code from being deployed

---

## Best Practices

- **Security:** Never hardcode tokens — use environment variables or a secrets manager
- **Code Quality:** Set Quality Gates to block merges when coverage drops below 80%
- **Scan on every pull request**, not just nightly builds
- **Fix issues as they appear** — do not let technical debt accumulate
- **Version all config files in Git**

# Experiment 11: Orchestration using Docker Compose & Docker Swarm

**Name:** Sourabh Saini
**Roll No:** R2142230968
**Course:** Containerization and DevOps

## Objective

Understand container orchestration by moving from Docker Compose to Docker Swarm. Learn how to deploy a stack, scale services, and observe self-healing in a Docker Swarm cluster using WordPress and MySQL setup.


## Prerequisites

- Docker installed with Swarm mode enabled
- The `docker-compose.yml` file from Experiment 6 (WordPress + MySQL)



## PART B – PRACTICAL (EXTENSION OF EXPERIMENT 6)



### Task 1: Initialize Docker Swarm

Swarm mode turns your current machine into a manager node of a cluster.

```bash
docker swarm init
```

Verify that your node is ready as a Swarm manager:

```bash
docker node ls
```
![](Lab/EXPERIMENT 11/image.png)



### Task 3: Deploy as a Stack (Not Just Compose)

In Swarm, we deploy a stack using the same Compose file. Swarm reads the file and creates services, which manage the containers automatically.

```bash
docker stack deploy -c docker-compose.yml wpstack
```
![](Lab/EXPERIMENT 11/image-1.png)



### Task 4: Verify the Deployment

List all services in the stack:

```bash
docker service ls
```
![](Lab/EXPERIMENT 11/image-2.png)

See detailed tasks (containers) for a specific service:

```bash
docker service ps wpstack_wordpress
```

See all running containers (notice they are managed by Swarm):

```bash
docker ps
```
![](Lab/EXPERIMENT 11/image-3.png)



### Task 5: Access WordPress

Open your browser and navigate to:
`http://localhost:8081`

You should see the WordPress setup screen.

![](Lab/EXPERIMENT 11/image-4.png)

---

### Task 6: Scale the Application (Swarm's Superpower)

Scale WordPress from 1 to 3 replicas using Swarm's orchestration.

```bash
docker service scale wpstack_wordpress=3
```
![](Lab/EXPERIMENT 11/image-5.png)

Verify the scaling:

```bash
docker service ls
docker service ps wpstack_wordpress
docker ps | grep wordpress
```
![](Lab/EXPERIMENT 11/image-6.png)

*Note: Swarm automatically balances traffic among all 3 containers on port 8081 without port conflicts.*



### Task 7: Test Self-Healing (Automatic Recovery)

Swarm automatically replaces failed containers. Let's test it:

**Step 1:** Find a WordPress container ID.
```bash
docker ps | grep wordpress
```

**Step 2:** Kill it to simulate a crash (replace `<container-id>`):
```bash
docker kill <container-id>
```
![](Lab/EXPERIMENT 11/image-7.png)

**Step 3:** Watch Swarm recreate it automatically:
```bash
docker service ps wpstack_wordpress
docker ps | grep wordpress
```
![](Lab/EXPERIMENT 11/image-8.png)

*Notice the killed container is shut down, and a new container is automatically created to maintain 3 replicas.*



### Task 8: Remove the Stack

Clean up the deployed stack and verify removal:

```bash
docker stack rm wpstack
docker service ls
docker ps
```
![](Lab/EXPERIMENT 11/image-9.png)





<div style='page-break-after: always;'></div>


# Experiment 12: Study and Analyse Container Orchestration using Kubernetes

**Name:** Sourabh Saini  
**Roll No:** R2142230968
**Course:** Containerization and DevOps  

---

## Objective

Learn why Kubernetes is used, its basic concepts, and how to deploy, scale, and fix apps using Kubernetes commands.

---

## Why Kubernetes over Docker Swarm?

| Reason | Explanation |
|--------|-------------|
| Industry standard | Most companies use Kubernetes |
| Powerful scheduling | Automatically decides where to run your app |
| Large ecosystem | Many tools and plugins available |
| Cloud-native support | Works on AWS, Google Cloud, Azure, etc. |

---

## Core Kubernetes Concepts (Simple Explanation)

| Docker Concept | Kubernetes Equivalent | What it means |
|---------------|----------------------|----------------|
| Container | Pod | A pod is a group of one or more containers. Smallest unit in K8s. |
| Compose service | Deployment | Describes how your app should run (e.g., 2 copies, which image to use) |
| Load balancing | Service | Exposes your app to the outside world or other pods |
| Scaling | ReplicaSet | Ensures a certain number of pod copies are always running |

---

## Hands-On Lab (Using k3d or Minikube)

> **Note:** We assume you already have `kubectl` and a cluster (k3d or Minikube) installed.

---

## PART A – Core Tasks

### Task 1: Create a Deployment

A deployment tells Kubernetes:
- Which container image to use (e.g., WordPress)
- How many copies (replicas) to run
- How to identify the pods (labels)

**Step 1:** Create the file `wordpress-deployment.yaml`

```yaml
# wordpress-deployment.yaml
apiVersion: apps/v1          # Which Kubernetes API to use
kind: Deployment             # Type of resource
metadata:
  name: wordpress            # Name of this deployment
spec:
  replicas: 2                # Run 2 identical pods
  selector:
    matchLabels:
      app: wordpress         # Pods with this label belong to this deployment
  template:                  # Template for the pods
    metadata:
      labels:
        app: wordpress       # Label applied to each pod
    spec:
      containers:
      - name: wordpress
        image: wordpress:latest   # Docker image
        ports:
        - containerPort: 80       # Port inside the container
```
![](Lab/EXPERIMENT 12/image.png)
**Step 2:** Apply the deployment

```bash
kubectl apply -f wordpress-deployment.yaml
```

> **What happens?** Kubernetes creates 2 pods running WordPress.

![](Lab/EXPERIMENT 12/image1.png)

---

### Task 2: Expose the Deployment as a Service

Pods are temporary (they can be deleted or recreated). A Service gives them a fixed IP and exposes them to the outside.

**Step 1:** Create the file `wordpress-service.yaml`

```yaml
# wordpress-service.yaml
apiVersion: v1
kind: Service
metadata:
  name: wordpress-service
spec:
  type: NodePort            # Exposes service on a port of each node (VM)
  selector:
    app: wordpress          # Send traffic to pods with this label
  ports:
    - port: 80              # Service port
      targetPort: 80        # Pod port
      nodePort: 30007       # External port (range: 30000-32767)
```
![](Lab/EXPERIMENT 12/image2.png)
**Step 2:** Apply the service

```bash
kubectl apply -f wordpress-service.yaml
```

---

### Task 3: Verify Everything

**Check if pods are running:**

```bash
kubectl get pods
```

![](Lab/EXPERIMENT 12/image3.png)

**Check the service:**

```bash
kubectl get svc
```
![](Lab/EXPERIMENT 12/image4.png)

**Access WordPress in your browser:**

```
http://localhost:30007
```

- **Minikube:** Usually `minikube ip`
- **k3d:** Usually `localhost`
![](Lab/EXPERIMENT 12/image5.png)

![](Lab/EXPERIMENT 12/image6.png)

---

### Task 4: Scale the Deployment

Increase the number of pods from 2 to 4:

```bash
kubectl scale deployment wordpress --replicas=4
```
![](Lab/EXPERIMENT 12/image7.png)
Verify:

```bash
kubectl get pods
```
![](Lab/EXPERIMENT 12/image8.png)

> You should now see 4 running pods.

> **Why scale?** More traffic → more copies → better performance.



---

### Task 5: Self-Healing Demonstration

Kubernetes automatically replaces failed pods.

**Step 1:** Get pod names

```bash
kubectl get pods
```

**Step 2:** Delete one pod (replace `<pod-name>`):

```bash
kubectl delete pod <pod-name>
```

**Step 3:** Check pods again:

```bash
kubectl get pods
```

> You will still see 4 pods — the deleted one was **automatically recreated**.

> **Why?** The deployment ensures the desired number (4) is always running.

![](Lab/EXPERIMENT 12/self.png)

---

## PART B – Cluster Information

```bash
kubectl get nodes
kubectl cluster-info
```

![](Lab/EXPERIMENT 12/cluster.png)

---

## PART C – Swarm vs Kubernetes (Comparison)

| Feature | Docker Swarm | Kubernetes |
|---------|-------------|------------|
| Setup | Very easy | More complex |
| Scaling | Basic | Advanced (auto-scaling) |
| Ecosystem | Small | Huge (monitoring, logging) |
| Industry use | Rare | Standard |

> **Verdict:** Learn Kubernetes — it's what companies use.

---

## PART D – Advanced Lab: Real Cluster with kubeadm

### Lab Requirements
- 2 or 3 virtual machines (e.g., VirtualBox, VMware)
- Ubuntu 22.04 or 24.04
- Each VM: 2+ CPU, 2+ GB RAM

### High-Level Steps

**Step 1:** Install `kubeadm`, `kubelet`, `kubectl` on all nodes

```bash
# Update system
sudo apt update

# Install required packages
sudo apt install -y apt-transport-https ca-certificates curl

# Add Kubernetes signing key
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.29/deb/Release.key | \
  sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg

# Add Kubernetes repository
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] \
  https://pkgs.k8s.io/core:/stable:/v1.29/deb/ /' | \
  sudo tee /etc/apt/sources.list.d/kubernetes.list

# Install kubeadm, kubelet, kubectl
sudo apt update
sudo apt install -y kubeadm kubelet kubectl

# Hold versions to prevent auto-update
sudo apt-mark hold kubeadm kubelet kubectl
```

![](Lab/EXPERIMENT 12/image9.png)

**Step 2:** Initialize the control plane (master node only)

```bash
sudo kubeadm init
```

This command:
- Sets up the control plane
- Generates a token for worker nodes to join
- Takes 2–3 minutes

**Step 3:** Set up kubeconfig (to use `kubectl`)

```bash
# Create .kube directory for your user
mkdir -p $HOME/.kube

# Copy admin config
sudo cp /etc/kubernetes/admin.conf $HOME/.kube/config

# Fix permissions
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

![](Lab/EXPERIMENT 12/image10.png)

Now you can run `kubectl get nodes` to see the master.

**Step 4:** Install a network plugin (required for pods to communicate)

```bash
kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml
```

![](Lab/EXPERIMENT 12/image11.png)

Wait 1–2 minutes for Calico to start.

**Step 5:** Join worker nodes

After `kubeadm init`, you'll see a join command like:

```bash
kubeadm join 192.168.1.100:6443 --token abcdef.0123456789abcdef \
    --discovery-token-ca-cert-hash sha256:...
```

Run that exact command on each worker node.

**Step 6:** Verify the cluster (on master)

```bash
kubectl get nodes
```

![](Lab/EXPERIMENT 12/image12.png)

Expected output:
```
NAME       STATUS   ROLES           AGE   VERSION
master     Ready    control-plane   5m    v1.29.0
worker1    Ready    <none>          2m    v1.29.0
worker2    Ready    <none>          2m    v1.29.0
```

---

## Summary of Commands (Cheat Sheet)

| Goal | Command |
|------|---------|
| Apply a YAML file | `kubectl apply -f file.yaml` |
| See all pods | `kubectl get pods` |
| See all services | `kubectl get svc` |
| Scale a deployment | `kubectl scale deployment <name> --replicas=N` |
| Delete a pod | `kubectl delete pod <pod-name>` |
| See all nodes | `kubectl get nodes` |
| Cluster info | `kubectl cluster-info` |

---

## Conclusion

In this experiment, we:

- Understood basic Kubernetes concepts (Pods, Deployments, Services, ReplicaSets)
- Deployed WordPress using a **Deployment** and **Service**
- **Scaled** the deployment from 2 to 4 replicas
- Demonstrated **self-healing** by deleting a pod and watching it auto-recover
- Compared **Docker Swarm** vs **Kubernetes**
- Learned how to build a real production-style cluster with `kubeadm`

**Next step:** Try deploying your own custom app (e.g., a simple Node.js or Python app).

