# 🧠 Task Manager Backend System — AI Enhanced (Emergence Assessment)

## 🚀 Overview

This is a backend system built with Flask for managing tasks. It includes full CRUD operations, AI-powered task analysis using OpenAI, and daily email notifications to assigned users. The project is structured for easy deployment and testing.

---

## 🛠️ Tech Stack

- **Backend:** Flask, Flask-SQLAlchemy
- **Database:** MySQL
- **AI Integration:** OpenAI GPT-3.5
- **Email Notifications:** Flask-Mail (Gmail SMTP)
- **Task Scheduler:** APScheduler
- **Testing:** Pytest

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/task-manager-backend.git
cd task-manager-backend
2. Create a .env File
Create a .env file in the root directory with the following content:

env
Copy
Edit
# MySQL Config
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=yourpassword
MYSQL_DB=task_manager

# OpenAI Key
OPENAI_API_KEY=your_openai_key

# Email Config (Gmail SMTP)
MAIL_USERNAME=yourgmail@gmail.com
MAIL_PASSWORD=your_gmail_app_password
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
⚠️ Note: Use a Gmail App Password (from https://myaccount.google.com/apppasswords)

3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Initialize the Database
bash
Copy
Edit
# Windows
set FLASK_APP=run.py

# Linux/macOS
export FLASK_APP=run.py

flask db init       # Only once
flask db migrate -m "initial"
flask db upgrade
5. Run the Server
bash
Copy
Edit
python run.py
📬 Email Notification System
A daily summary email is automatically sent at 9:00 AM (if any tasks exist).

You can manually test it using this endpoint:

bash
Copy
Edit
GET http://localhost:5000/send-email-test
🤖 AI Features
Each task is analyzed using OpenAI’s GPT-3.5:

Auto-generates ai_analysis

Calculates urgency_score

Predicts ai_analyzed_priority

📮 API Endpoints
Method	Endpoint	Description
POST	/tasks	Create a new task
GET	/tasks	Get all tasks
GET	/tasks/<id>	Get a specific task
PUT	/tasks/<id>	Update a task
DELETE	/tasks/<id>	Delete a task
GET	/send-email-test	Send daily summary email

🧪 Testing
Run all tests using:

bash
Copy
Edit
pytest tests/
🔬 Postman Collection
A Postman collection is provided for testing:

bash
Copy
Edit
postman/task_manager_collection.json
You can import it directly into Postman and test all endpoints.