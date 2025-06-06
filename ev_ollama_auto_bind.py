
import os
import subprocess
import socket
from flask import Flask, request, jsonify

# Helper: Find an available port starting from 8081
def find_open_port(start=8081, max_tries=20):
    for port in range(start, start + max_tries):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(("127.0.0.1", port)) != 0:
                return port
    return None

# Setup EVBot Flask Server on open port
def start_evbot_flask(port):
    app = Flask(__name__)

    @app.route('/evbot/command', methods=['POST'])
    def process_command():
        data = request.get_json()
        spell = data.get("spell", "")
        if spell == "say_hi":
            return jsonify({"message": "🔮 EVBot online via auto-bind on port " + str(port)})
        return jsonify({"result": "Unknown spell"})

    app.run(host="127.0.0.1", port=port)

# Try to find open port for Flask
ev_port = find_open_port()

if ev_port:
    print(f"✅ Binding EVBot to port {ev_port}")
    import threading
    flask_thread = threading.Thread(target=start_evbot_flask, args=(ev_port,))
    flask_thread.daemon = True
    flask_thread.start()
else:
    print("❌ No open port found for EVBot Flask")

# Try to start Ollama on new port if needed
ollama_ports = [5050, 5000]
ollama_started = False

for port in ollama_ports:
    try:
        subprocess.run(["ollama", "run", "--host", f"0.0.0.0:{port}"], check=True)
        print(f"✅ Ollama started on port {port}")
        ollama_started = True
        break
    except Exception as e:
        print(f"⚠️ Ollama failed to start on port {port}: {str(e)}")

if not ollama_started:
    print("❌ Ollama could not be started on any designated ports")
