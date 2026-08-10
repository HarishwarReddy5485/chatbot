from django.shortcuts import render
import requests
import os 
def chatbot(request):

    answer = ""

    if request.method == "POST":

        api_key = os.getenv("GEMINI_API_KEY", "your_fallback_key")

        URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"

        user_input = request.POST.get("question")

        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [
                        {
                            "text": user_input
                        }
                    ]
                }
            ]
        }

        response = requests.post(URL, json=payload)

        if response.status_code == 200:
            data = response.json()
            answer = data["candidates"][0]["content"]["parts"][0]["text"]
        else:
            answer = f"Error ({response.status_code}): {response.text}"

    return render(request, "index.html", {"answer": answer})
