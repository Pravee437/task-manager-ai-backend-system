# 🧠 Task Manager AI Backend System

An AI-powered task management backend built with Flask, SQLAlchemy, and MySQL. This system supports full CRUD operations, OpenAI integration for smart task analysis, and automated email notifications using Flask-Mail.

> 🚀 Built as part of the Emergence Software Assessment

---

## ⚙️ Features

- ✅ RESTful API with Flask
- 🧠 AI-based priority, risk, and urgency analysis using OpenAI
- 📬 Daily email summaries using Flask-Mail
- 🔒 Environment variable support via `.env`
- 🧪 Unit testing with `pytest`
- 📊 SQLAlchemy models with Flask-Migrate

---

## 📁 Project Structure

task-manager-ai-backend-system/
├── app/
│ ├── init.py
│ ├── models.py
│ ├── routes.py
│ ├── config.py
│ ├── ai.py
│ └── email_service.py
├── migrations/
├── tests/
│ └── test_routes.py
├── .env # Not committed — contains secrets
├── .gitignore
├── requirements.txt
└── run.py


---

## 🔧 Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Pravee437/task-manager-ai-backend-system.git
cd task-manager-ai-backend-system


2️⃣ Create a virtual environment
python -m venv .venv
source .venv/bin/activate     # On Windows: .venv\Scripts\activate


3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Configure your .env file

Create a .env file and add:
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_mysql_password
MYSQL_DB=task_manager

MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password

OPENAI_API_KEY=your_openai_api_key
⚠️ Never commit your real .env file.

5️⃣ Run migrations

flask db init       # Only once
flask db migrate -m "Initial migration"
flask db upgrade

6️⃣ Start the server

python run.py
📬 Test Email Endpoint
Send a test daily summary email (if any tasks assigned):


GET /send-email-test
📦 API Endpoints
Method	Endpoint	Description
GET	/	Welcome message
POST	/tasks	Create a new task
GET	/tasks	Get all tasks
GET	/tasks/<id>	Get a task by ID
PUT	/tasks/<id>	Update a task
DELETE	/tasks/<id>	Delete a task
GET	/send-email-test	Trigger test email summary

📚 API Documentation with Sample Requests/Responses
🔹 GET /
Description: Health check for the API.
Response:

{
  "message": "Task Management API is running!"
}
🔹 POST /tasks
Description: Create a new task.
Request Body:


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
Response:


{
  "message": "Task created successfully"
}
🔹 GET /tasks
Description: Retrieve all tasks.
Response:

[
  {
    "id": 1,
    "title": "Complete Assessment",
    "status": "pending",
    "priority": "high",
    "assigned_to": "Praveen",
    "due_date": "2025-12-31",
    "ai_analyzed_priority": "urgent",
    ...
  }
]
🔹 GET /tasks/<id>
Description: Retrieve a single task by ID.
Example: GET /tasks/1
Response:


{
  "id": 1,
  "title": "Complete Assessment",
  "description": "Finish all tasks in the backend project",
  "status": "pending",
  "priority": "high",
  ...
}
🔹 PUT /tasks/<id>
Description: Update a task.
Example: PUT /tasks/1
Request Body:


{
  "status": "in_progress"
}
Response:


{
  "message": "Task updated successfully"
}
🔹 DELETE /tasks/<id>
Description: Delete a task.
Example: DELETE /tasks/1
Response:


{
  "message": "Task deleted successfully"
}
🔹 GET /send-email-test
Description: Sends a test summary email for today's tasks.

Response:


{
  "message": "Daily summary email sent (if tasks found)."
}

🧪 Running Tests

pytest
✅ Running Tests
This project uses pytest for testing.

🔧 Test Setup
Make sure your virtual environment is activated:
source .venv/bin/activate    # Mac/Linux
.venv\Scripts\activate       # Windows
Set the PYTHONPATH to the current directory so that modules resolve correctly:
# Windows
set PYTHONPATH=.

# Mac/Linux
export PYTHONPATH=.
Run all tests:

pytest tests/
🧪 Notes
Uses an in-memory SQLite database (sqlite:///:memory:) for isolated, fast tests.

Tests include:

✅ test_ai.py – AI task analysis

✅ test_api.py – API endpoint checks

✅ test_email.py – Email summary sending

Deprecation warnings (e.g., datetime.utcnow() warning) do not affect test results but may be addressed in future updates.


👨‍💻 Author
Praveen Rupineni
GitHub • LinkedIn

📄 License
This project is part of a private assessment and is not currently open for commercial use.
