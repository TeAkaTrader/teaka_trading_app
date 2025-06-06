from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def query_ollama(prompt, model="llama3"):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(url, json=data)
        return response.json().get("response", "[No response from Ollama]")
    except Exception as e:
        return f"[Ollama error: {str(e)}]"

@app.route('/ev_remote/ollama', methods=['POST'])
def ask_ollama():
    data = request.json
    prompt = data.get("prompt", "")
    model = data.get("model", "llama3")
    response = query_ollama(prompt, model)
    return jsonify({"response": response})
