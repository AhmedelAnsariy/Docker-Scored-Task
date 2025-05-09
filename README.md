# 🧪 FastAPI Product API

A simple RESTful API built with **FastAPI**, using **PostgreSQL** as the database and **Redis** for caching. The application is containerized with **Docker** and **nginx**.

my-fastapi-app/
├── app/
│ 
│   ├── main.py         
│   ├── models.py/
│   |___database.py.py    
|   
│  
├── Dockerfile              
├── docker-compose.yml       
├── nginx/
│   └── default.conf         
│
├── requirements.txt         
└── README.md                 


## 📦 Tech Stack

- **FastAPI** – Web framework  
- **PostgreSQL** – Relational database  
- **Redis** – In-memory data store for caching  
- **Docker** – Containerization  
- **Uvicorn** – ASGI server  
- **Nginx** – Reverse proxy  

---

## 🚀 Multi-stage Docker Build

This project uses a **multi-stage Docker build** to optimize the image size and improve the efficiency of the build process.

### How it works:

1. **Stage 1: Build**
   - A `builder` stage is used to install the required dependencies from the `requirements.txt` file.
   - Python packages are installed with the `--user` flag to avoid installation in the system-wide environment.
   - This stage ensures that only the necessary dependencies are included in the final image.

2. **Stage 2: Final**
   - A minimal Python image is used to build the final Docker image.
   - The dependencies installed in the `builder` stage are copied to this stage to ensure a clean and lightweight image.
   - The application code is then copied, and the application is started using **Uvicorn**.

This approach reduces the size of the final Docker image by eliminating unnecessary build tools and files.

### Benefits:
- Smaller image size due to the exclusion of build dependencies in the final image.
- Faster deployment and easier maintenance due to the separation of concerns in the build process.
- Cleaner and more organized Dockerfile.


The application exposes the following 3 endpoints:


The application exposes the following 3 main endpoints:

🟢 GET / – Health check or root endpoint
This endpoint is used to verify that the server is running and responsive.

🟢 GET /products – Retrieve all products
This endpoint returns a list of all products available in the database.

🔵 POST /product – Create a new product
This endpoint allows the creation of a new product. You need to send a JSON body with the product detail


## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/AhmedelAnsariy/Docker-Scored-Task.git
cd my-fastapi-app


'''' start project 

# 🔨 Build Docker Images
docker-compose build

# 🚀 Run All Services
docker-compose up

# 📄 View Logs
docker-compose logs -f

# 🛑 Stop Containers
docker-compose down

# 💣 Stop & Remove Containers + Volumes (DB & Redis)
docker-compose down -v


🔒 Environment Variables
I have added a .env file to store sensitive configuration settings and environment variables for the project. To ensure that these settings are not exposed, the .env file is included in the .gitignore file, preventing it from being committed to the Git repository



## 🔒 Trivy Security Scanning Commands

To ensure the security of your Docker images and files, you can use Trivy for vulnerability scanning.

### 1. Scan a Docker Image for Vulnerabilities:
trivy image <image-name>

### 2. Save the Scan Results in a JSON File:
trivy image -f json -o result.json <image-name>

### 3. Scan a Docker Image for High or Critical Severity Vulnerabilities Only:
trivy image --severity HIGH,CRITICAL <image-name>



