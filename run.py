
from app import create_app, db, mail
from app.email_service import send_daily_summary
from apscheduler.schedulers.background import BackgroundScheduler

app = create_app()

# Avoid circular import by calling send_daily_summary here
scheduler = BackgroundScheduler()
scheduler.add_job(lambda: send_daily_summary(app, mail, db), trigger='cron', hour=9, minute=0)
scheduler.start()

if __name__ == "__main__":
    app.run(debug=True)
