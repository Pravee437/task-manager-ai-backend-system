from app.ai import analyze_task
from datetime import datetime

def test_analyze_task():
    result = analyze_task("Fix critical bug before release", datetime(2025, 7, 25))
    assert isinstance(result, dict)
    assert "ai_analysis" in result
    assert "urgency_score" in result
    assert "ai_analyzed_priority" in result
