
import pytest
from app import create_app, db, mail
from app.email_service import send_daily_summary

class TestingConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SUPPRESS_SEND = True
    MAIL_DEFAULT_SENDER = "test@example.com"
    MAIL_SERVER = "localhost"
    MAIL_PORT = 8025
    OPENAI_API_KEY = "test"

@pytest.fixture
def app_context():
    app = create_app(config_class=TestingConfig)
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()

def test_send_email_summary_runs(app_context):
    try:
        send_daily_summary(app_context, mail, db)
    except Exception as e:
        pytest.fail(f"Email summary failed: {e}")
