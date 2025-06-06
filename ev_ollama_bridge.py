import requests

def query_ollama(prompt, model="llama3"):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=data)
    return response.json().get("response", "[No Response]")

# Example test
if __name__ == "__main__":
    result = query_ollama("What minerals are associated with pegmatites?")
    print("🧠 Ollama says:", result)
