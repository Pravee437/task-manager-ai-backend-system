# 🧠 Task Manager AI Backend System

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)

**An AI-powered task management backend built with Flask, SQLAlchemy, and MySQL**

> 🚀 **Built as part of the Emergence Software Assessment**

[Features](#-features) • [Setup](#-setup-instructions) • [API Docs](#-api-documentation-with-sample-requestsresponses) • [Testing](#-running-tests)

</div>

---

## ⚙️ Features

<table>
<tr>
<td width="50%">

### 🔧 **Core Backend**
- ✅ RESTful API with Flask
- 📊 SQLAlchemy models with Flask-Migrate
- 🔒 Environment variable support via `.env`
- 🧪 Unit testing with `pytest`

</td>
<td width="50%">

### 🤖 **AI & Automation**
- 🧠 AI-based priority, risk, and urgency analysis using OpenAI
- 📬 Daily email summaries using Flask-Mail
- 🔍 Smart task analysis and categorization

</td>
</tr>
</table>

---

## 📁 Project Structure

```
task-manager-ai-backend-system/
├── 📁 app/
│   ├── __init__.py          # Flask app initialization
│   ├── models.py            # Database models
│   ├── routes.py            # API endpoints
│   ├── config.py            # Configuration
│   ├── ai.py                # OpenAI integration
│   └── email_service.py     # Email automation
├── 📁 migrations/           # Database migrations
├── 📁 tests/
│   └── test_routes.py       # API tests
├── .env                     # Environment secrets (not committed)
├── .gitignore
├── requirements.txt         # Dependencies
└── run.py                   # Application entry point
```

---

## 🔧 Setup Instructions

### Prerequisites
- Python 3.8+
- MySQL Server
- OpenAI API Key

### 1️⃣ **Clone the repository**

```bash
git clone https://github.com/Pravee437/task-manager-ai-backend-system.git
cd task-manager-ai-backend-system
```

### 2️⃣ **Create a virtual environment**

```bash
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate     # On macOS/Linux
# .venv\Scripts\activate      # On Windows
```

### 3️⃣ **Install dependencies**

```bash
pip install -r requirements.txt
```

### 4️⃣ **Configure your .env file**

Create a `.env` file in the root directory:

```env
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_mysql_password
MYSQL_DB=task_manager

MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password

OPENAI_API_KEY=your_openai_api_key
```

> ⚠️ **Important:** Never commit your real `.env` file with sensitive credentials

### 5️⃣ **Run migrations**

```bash
flask db init                           # Only run once
flask db migrate -m "Initial migration"
flask db upgrade
```

### 6️⃣ **Start the server**

```bash
python run.py
```

🎉 **Success!** Server running at `http://localhost:5000`

### 📬 **Test Email Endpoint**

Send a test daily summary email (if any tasks assigned):

```bash
GET http://localhost:5000/send-email-test
```

---

## 📦 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Welcome message |
| `POST` | `/tasks` | Create a new task |
| `GET` | `/tasks` | Get all tasks |
| `GET` | `/tasks/<id>` | Get a task by ID |
| `PUT` | `/tasks/<id>` | Update a task |
| `DELETE` | `/tasks/<id>` | Delete a task |
| `GET` | `/send-email-test` | Trigger test email summary |

---

## 📚 API Documentation with Sample Requests/Responses

**Base URL:** `http://localhost:5000`

### 🟢 **GET /** - Health Check
**Description:** API health check  
**URL:** `http://localhost:5000/`

**Response:**
```json
{
  "message": "Task Management API is running!"
}
```

### 🟡 **POST /tasks** - Create Task
**Description:** Create a new task  
**URL:** `http://localhost:5000/tasks`  
**Method:** POST

**Request Body:**
```json
{
  "title": "Complete Assessment",
  "description": "Finish all tasks in the backend project",
  "priority": "high",
  "assigned_to": "Praveen",
  "assigned_email": "praveen@example.com",
  "due_date": "2025-12-31",
  "department": "Engineering",
  "estimated_hours": 5
}
```

**Response:**
```json
{
  "message": "Task created successfully"
}
```

### 🟢 **GET /tasks** - Get All Tasks
**Description:** Get all tasks  
**URL:** `http://localhost:5000/tasks`  
**Method:** GET

**Response:**
```json
[
  {
    "id": 1,
    "title": "Complete Assessment",
    "status": "pending",
    "priority": "high",
    "assigned_to": "Praveen",
    "ai_analyzed_priority": "urgent",
    "due_date": "2025-12-31"
  }
]
```

### 🟢 **GET /tasks/<id>** - Get Task by ID
**Description:** Get a specific task by ID  
**URL:** `http://localhost:5000/tasks/1`  
**Method:** GET

**Response:**
```json
{
  "id": 1,
  "title": "Complete Assessment",
  "status": "pending",
  "priority": "high",
  "assigned_to": "Praveen",
  "ai_analyzed_priority": "urgent"
}
```

### 🔄 **PUT /tasks/<id>** - Update Task
**Description:** Update a task  
**URL:** `http://localhost:5000/tasks/1`  
**Method:** PUT

**Request Body:**
```json
{
  "status": "in_progress"
}
```

**Response:**
```json
{
  "message": "Task updated successfully"
}
```

### ❌ **DELETE /tasks/<id>** - Delete Task
**Description:** Delete a task by ID  
**URL:** `http://localhost:5000/tasks/1`  
**Method:** DELETE

**Response:**
```json
{
  "message": "Task deleted successfully"
}
```

### 📬 **GET /send-email-test** - Test Email
**Description:** Send a test daily summary email for today's assigned tasks  
**URL:** `http://localhost:5000/send-email-test`  
**Method:** GET

**Response:**
```json
{
  "message": "Daily summary email sent (if tasks found)."
}
```

---

## 🧪 Running Tests

### Quick Test
```bash
pytest
```

### ✅ Detailed Testing Guide

This project uses **pytest** for comprehensive testing.

#### 🔧 **Test Setup**

1. **Activate your virtual environment:**
   ```bash
   source .venv/bin/activate    # Mac/Linux
   .venv\Scripts\activate       # Windows
   ```

2. **Set the PYTHONPATH:**
   ```bash
   # Windows
   set PYTHONPATH=.
   
   # Mac/Linux
   export PYTHONPATH=.
   ```

3. **Run all tests:**
   ```bash
   pytest tests/
   ```

#### 🧪 **Test Features**
- Uses an **in-memory SQLite database** (`sqlite:///:memory:`) for isolated, fast tests
- **Test Coverage:**
  - ✅ `test_ai.py` – AI task analysis
  - ✅ `test_api.py` – API endpoint checks  
  - ✅ `test_email.py` – Email summary sending

#### 📝 **Notes**
- Deprecation warnings (e.g., `datetime.utcnow()` warning) do not affect test results but may be addressed in future updates
- All tests run independently with clean database state

---

## 👨‍💻 Author

**Praveen Rupineni**

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Pravee437)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/praveen-rupineni)

---

## 📄 License

This project is part of a private assessment and is not currently open for commercial use.

---

<div align="center">

**🚀 Built for Emergence Software Assessment**

*Showcasing AI-powered backend development with Flask and OpenAI*

---

**💼 I am excited about the opportunity to join Emergence and would be thrilled to contribute to your innovative projects. Thank you for taking the time to review this technical assessment - I look forward to discussing how my skills can add value to your team!**

</div>
