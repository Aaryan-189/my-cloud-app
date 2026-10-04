# Cloud Deployment Assessment: Containerized Microservice

**Author:** Aaryan Saxena  
**Roll Number:** 27004  

## Overview
This project is a containerized Python microservice deployed to the cloud. It features a REST API built with FastAPI, strict data validation using Pydantic, and an interactive frontend dashboard built with Tailwind CSS. The application is packaged using Docker (configured with a secure, non-root user) and hosted on an AWS EC2 instance. 

A CI/CD pipeline powered by GitHub Actions automatically tests the code on every push, ensuring continuous stability before deployment.

## Architecture
`Client Browser` ➔ `AWS EC2 (Ubuntu)` ➔ `Docker Container (Port 8000)` ➔ `FastAPI Server`

## Key Features
* **Interactive UI:** A custom `/ui` endpoint serves a dark-mode Tailwind CSS dashboard for real-time API interaction.
* **Continuous Integration:** GitHub Actions pipeline runs automated Pytest cases with dependency caching to block failing code pushes.
* **Security First:** The Docker container executes as a restricted, non-root user.
* **Data Validation:** Incoming POST requests are strictly validated using Pydantic models.
* **CORS Enabled:** Cross-Origin Resource Sharing is configured to support future external frontend integrations.

## Live Deployment
The live application is currently accessible at: 
**http://13.60.202.32:8000/ui**

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Root endpoint returning a Hello World message. |
| `GET` | `/health` | Returns the health status and current API version. |
| `GET` | `/items/{id}` | Fetches an item by ID (must be a positive integer). |
| `POST` | `/echo` | Accepts a JSON payload (`name`, `project`) and echoes it back. |
| `GET` | `/ui` | Serves the interactive HTML/Tailwind frontend dashboard. |

## How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/](https://github.com/)<YOUR-USERNAME>/my-cloud-app.git
   cd my-cloud-app