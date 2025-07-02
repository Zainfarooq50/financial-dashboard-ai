import os
import requests
from config import api_key


# ---------------- AI Financial Insights ----------------
def get_ai_insights(summary_text):
    """
    Uses GPT to generate expert financial insights from a summary.
    """
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    prompt = (
        "You are a financial expert. Based on the following summary, provide insights "
        "on profitability, risks, and areas for improvement:\n\n" + summary_text
    )

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You provide expert financial analysis."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 300
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"❌ AI Error: {e}")
        return "⚠️ AI could not generate insights."
