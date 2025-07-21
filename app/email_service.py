
from flask_mail import Message
from .models import Task
from datetime import datetime
from .ai import analyze_task

def send_daily_summary(app, mail, db):
    with app.app_context():
        users = db.session.query(Task.assigned_email).distinct()

        for user_email, in users:
            if not user_email:
                continue

            tasks = db.session.query(Task).filter_by(assigned_email=user_email).filter(Task.status != 'completed').all()
            if not tasks:
                continue

            task_text = "\n".join([f"- {task.title} (Due: {task.due_date.strftime('%Y-%m-%d')})" for task in tasks])
            ai_response = analyze_task(task_text, datetime.utcnow())

            summary = ai_response.get("ai_analysis", "No insights")
            urgency = ai_response.get("urgency_score", 0)

            msg = Message(
                subject="Daily Task Summary",
                sender=app.config['MAIL_USERNAME'],
                recipients=[user_email],
                body=f"""
Hi,

🔍 Summary:
{summary}

📌 Urgency Score: {urgency}

📋 Tasks:
{task_text}

Regards,
TaskBot
"""
            )
            mail.send(msg)

