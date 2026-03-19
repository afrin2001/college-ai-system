import requests

def chatbot_reply(message):
    prompt = f"""
You are an AI assistant for Vallalar Arts and Science College.

Details:
- Location: Vadalur, Tamil Nadu
- Courses: BCA, BBA, B.Com, B.Sc, BA, M.Com
- Admissions are open

Answer clearly.

User: {message}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]
