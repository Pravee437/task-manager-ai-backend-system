from flask import Blueprint, request, jsonify
from .models import Task
from datetime import datetime
from .ai import analyze_task  # ✅ AI integration
from .email_service import send_daily_summary
from . import db, mail
from flask import current_app

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route("/", methods=["GET"])
def index():
    return {"message": "Task Management API is running!"}

@api_blueprint.route('/', methods=['GET'])
def home():
    return {"message": "Task Management Backend API is running!"}

@api_blueprint.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    try:
        new_task = Task(
            title=data['title'],
            description=data.get('description'),
            priority=data.get('priority', 'medium'),
            assigned_to=data.get('assigned_to'),
            assigned_email=data.get('assigned_email'),
            due_date=datetime.strptime(data['due_date'], "%Y-%m-%d") if data.get('due_date') else None,
            department=data.get('department'),
            estimated_hours=data.get('estimated_hours')
        )

        # ✅ AI Integration Step: Analyze task
        if new_task.description and new_task.due_date:
            ai_result = analyze_task(new_task.description, new_task.due_date)
            new_task.ai_analyzed_priority = ai_result['ai_analyzed_priority']
            new_task.ai_analysis = ai_result['ai_analysis']
            new_task.urgency_score = ai_result['urgency_score']

        db.session.add(new_task)
        db.session.commit()
        return jsonify({"message": "Task created successfully", "task_id": new_task.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@api_blueprint.route('/tasks', methods=['GET'])
def get_all_tasks():
    tasks = Task.query.all()
    return jsonify([{
        "id": t.id,
        "title": t.title,
        "status": t.status,
        "priority": t.priority,
        "assigned_to": t.assigned_to,
        "due_date": t.due_date.strftime("%Y-%m-%d") if t.due_date else None
    } for t in tasks])


@api_blueprint.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify({
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "status": task.status,
        "priority": task.priority,
        "ai_analyzed_priority": task.ai_analyzed_priority,
        "assigned_to": task.assigned_to,
        "assigned_email": task.assigned_email,
        "created_at": task.created_at.strftime("%Y-%m-%d %H:%M"),
        "due_date": task.due_date.strftime("%Y-%m-%d") if task.due_date else None,
        "completed_at": task.completed_at.strftime("%Y-%m-%d %H:%M") if task.completed_at else None,
        "department": task.department,
        "estimated_hours": task.estimated_hours,
        "urgency_score": task.urgency_score,
        "ai_analysis": task.ai_analysis
    })


@api_blueprint.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    data = request.get_json()
    try:
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.status = data.get('status', task.status)
        task.priority = data.get('priority', task.priority)
        task.ai_analyzed_priority = data.get('ai_analyzed_priority', task.ai_analyzed_priority)
        task.assigned_to = data.get('assigned_to', task.assigned_to)
        task.assigned_email = data.get('assigned_email', task.assigned_email)
        task.due_date = datetime.strptime(data['due_date'], "%Y-%m-%d") if data.get('due_date') else task.due_date
        task.completed_at = datetime.strptime(data['completed_at'], "%Y-%m-%d %H:%M") if data.get('completed_at') else task.completed_at
        task.department = data.get('department', task.department)
        task.estimated_hours = data.get('estimated_hours', task.estimated_hours)
        task.urgency_score = data.get('urgency_score', task.urgency_score)
        task.ai_analysis = data.get('ai_analysis', task.ai_analysis)
        db.session.commit()
        return jsonify({"message": "Task updated successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@api_blueprint.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted successfully"})



@api_blueprint.route('/send-email-test', methods=['GET'])
def test_email_now():
    send_daily_summary(current_app._get_current_object(), mail, db)
    return {"message": "Test email sent (if any tasks are assigned)"}


