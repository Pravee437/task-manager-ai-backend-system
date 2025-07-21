from datetime import datetime
from . import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.Enum('pending', 'in_progress', 'completed', 'overdue'), default='pending')
    priority = db.Column(db.Enum('low', 'medium', 'high', 'urgent'), default='medium')
    ai_analyzed_priority = db.Column(db.Enum('low', 'medium', 'high', 'urgent'))
    assigned_to = db.Column(db.String(100))
    assigned_email = db.Column(db.String(120))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    due_date = db.Column(db.DateTime)
    completed_at = db.Column(db.DateTime)
    department = db.Column(db.String(50))
    estimated_hours = db.Column(db.Float)
    ai_analysis = db.Column(db.Text)
    urgency_score = db.Column(db.Float)
