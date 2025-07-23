# vision.py

import requests
from functions.config import OPENAI_API_KEY

def process_image_with_openai(image_base64: str, prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "gpt-4-turbo",
        "messages": [
            {"role": "system", "content": prompt},
            {
                "role": "user",
                "content": [{"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"}}],
            },
        ],
        "max_tokens": 500,
    }

    try:
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print("Error processing image with OpenAI:", e)
        raise
