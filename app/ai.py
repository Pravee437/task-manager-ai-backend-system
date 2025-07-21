import openai
import os
import json
from datetime import datetime
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_task(description, due_date):
    days_left = (due_date - datetime.utcnow()).days

    prompt = f"""
You are an assistant helping prioritize tasks. Analyze the following task:

Description: {description}
Days Until Due: {days_left}

1. Based on the description and urgency, classify priority as: low, medium, high, or urgent.
2. Give a short analysis on potential risk or delay.
3. Estimate urgency score between 0.0 (low) and 1.0 (critical).

Return as JSON in this format:
{{
  "ai_analyzed_priority": "...",
  "ai_analysis": "...",
  "urgency_score": ...
}}
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    result_text = response.choices[0].message.content
    return json.loads(result_text)
