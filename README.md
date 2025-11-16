# url-shortener

A simple full-stack URL shortener built with **FastAPI** (Python) for the backend  
and **React + Vite** for the frontend. The app lets users shorten long URLs and get quick redirects via short codes.

---

## Quick Start (with Docker Compose)

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/)  
- [Docker Compose](https://docs.docker.com/compose/)

### 1️⃣ Clone the repository
```bash
git clone https://github.com/ogitc/url-shortener.git
cd url-shortener
```

### 2️⃣ Build and run both services
```bash
docker compose up --build
```

This will:

Build the backend (FastAPI) image

Build the frontend (React + Vite → served by Nginx) image

Start both containers and link them automatically

### 3️⃣ Access the app
| Service  | URL                                            | Description                   |
| -------- | ---------------------------------------------- | ----------------------------- |
| Frontend | [http://localhost:5173](http://localhost:5173) | React interface               |
| Backend  | [http://localhost:8000/docs](http://localhost:8000/docs) | FastAPI API docs|


### Tests
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pytest -q
```