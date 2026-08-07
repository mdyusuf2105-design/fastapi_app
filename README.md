# 🚀 FastAPI Asynchronous Job Queue System

A scalable asynchronous job processing system built with **FastAPI**, **Celery**, **Redis**, and **MySQL**. The application allows users to submit background jobs, process them asynchronously using Celery workers, prioritize jobs, retry failed jobs automatically, and monitor job statistics through REST APIs.

---

# 📌 Features

- Submit background jobs through REST APIs
- Asynchronous job processing using Celery
- Redis message broker
- Priority-based queue (High, Medium, Low)
- FIFO queue processing
- Automatic retry mechanism
- Configurable retry limits
- Concurrent worker execution
- Job status tracking
- Dashboard API for monitoring jobs
- Structured logging
- Error handling and failure tracking

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| FastAPI | REST API |
| Celery | Background task processing |
| Redis | Message Broker |
| MySQL | Database |
| SQLAlchemy | ORM |
| Pydantic | Request Validation |

---

# 🏗 Project Architecture

```
                Client
                   │
                   ▼
            FastAPI Routes
                   │
                   ▼
             Service Layer
                   │
                   ▼
          Celery + Redis Queue
                   │
                   ▼
            Celery Workers
                   │
                   ▼
                MySQL
```

---

# 📂 Project Structure

```
fastapi_app/
│
├── core/
│   ├── config.py
│   ├── database.py
│   └── logger.py
│
├── models/
│   ├── job.py
│   └── user.py
│
├── routes/
│   ├── auth.py
│   ├── jobs.py
│   └── users.py
│
├── schemas/
│   └── job.py
│
├── services/
│   ├── job_services.py
│   └── dashboard_service.py
│
├── workers/
│   ├── celery_app.py
│   └── tasks.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# 🔄 Queue Processing Flow

```
Client

↓

POST /jobs

↓

Create Job

↓

Save Job in Database

↓

Send Task to Redis Queue

↓

Celery Worker

↓

Running

↓

Completed / Failed
```

---

# 👷 Worker Design

The application separates API requests from background processing.

1. FastAPI receives the request.
2. Job information is stored in MySQL.
3. Celery sends the task to Redis.
4. A Celery worker consumes the task.
5. Worker updates the job status:
   - Pending
   - Running
   - Completed
   - Failed

This design ensures the API remains responsive while long-running tasks execute in the background.

---

# 📋 API Endpoints

## General

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome endpoint |
| GET | `/health` | Health check |
| GET | `/version` | API version |

---

## Jobs

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/jobs` | Create a new job |
| GET | `/jobs` | Get all jobs |
| GET | `/jobs/dashboard` | Dashboard statistics |

---

# 📊 Dashboard

The dashboard endpoint provides:

- Total Jobs
- Pending Jobs
- Running Jobs
- Completed Jobs
- Failed Jobs
- Average Processing Time
- Queue Statistics
  - High
  - Medium
  - Low

Example response:

```json
{
  "total_jobs": 20,
  "pending_jobs": 1,
  "running_jobs": 0,
  "completed_jobs": 18,
  "failed_jobs": 1,
  "average_processing_time_seconds": 20.0,
  "queue_statistics": {
    "high": 8,
    "medium": 7,
    "low": 5
  }
}
```

---

# 🔁 Retry Mechanism

Failed jobs are automatically retried using Celery.

- Maximum Retries: **3**
- Retry Delay: **5 seconds**

If retries are exhausted:

- Job Status → Failed
- Retry Count updated
- Error Message stored in database

---

# 📜 Logging

The project implements structured logging using Python's logging module.

Example logs:

```
INFO     Processing Job 20

INFO     Completed Job 20

WARNING  Retry 1 for Job 21

WARNING  Retry 2 for Job 21

WARNING  Retry 3 for Job 21

ERROR    Job 21 failed after 3 retries
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/mdyusuf2105-design/fastapi_app.git
```

```
cd fastapi_app
```

---

## Create Virtual Environment

```bash
python3 -m venv venv
```

Activate

Mac/Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment

Create a `.env` file.

Example:

```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=fastapi_db
DB_USER=root
DB_PASSWORD=your_password
```

---

## Start FastAPI

```bash
uvicorn main:app --reload
```

---

## Start Redis

```bash
redis-server
```

---

## Start Celery Worker

```bash
celery -A workers.celery_app worker -Q high,medium,low --loglevel=info
```

---

# ✅ Assignment Requirements Completed

- REST API
- Asynchronous Job Processing
- Redis Queue
- Celery Workers
- Priority Queues
- FIFO Processing
- Retry Mechanism
- Worker System
- Monitoring Dashboard
- Structured Logging
- Error Handling
- Clean Architecture

---

# 📈 Scalability

The application is designed to scale by:

- Running multiple Celery workers
- Increasing worker concurrency
- Using Redis as a distributed message broker
- Separating API and worker processes

---

# 👨‍💻 Author

**Mohamed Yusuf U**

GitHub: https://github.com/mdyusuf2105-design