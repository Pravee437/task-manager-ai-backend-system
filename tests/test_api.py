

import pytest
from app import create_app, db
from app.config import TestingConfig

@pytest.fixture
def client():
    app = create_app(TestingConfig)
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Task Management API is running!' in response.data

def test_create_task(client):
    payload = {
        "title": "Test Task",
        "description": "Simple task for testing",
        "priority": "high",
        "assigned_to": "Tester",
        "assigned_email": "test@example.com",
        "due_date": "2025-12-31",
        "department": "QA",
        "estimated_hours": 5
    }
    response = client.post('/tasks', json=payload)
    assert response.status_code == 201
    assert b'Task created successfully' in response.data

