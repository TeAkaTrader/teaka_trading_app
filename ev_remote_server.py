
from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

COMMAND_FILE = 'E:/EchoVault/command.json'
RESPONSE_FILE = 'E:/EchoVault/response.json'
BRAIN_FILE = 'E:/EV_Files/ev_virtual_brain.json'

def load_brain():
    if os.path.exists(BRAIN_FILE):
        with open(BRAIN_FILE, 'r') as f:
            return json.load(f)
    return {"error": "Brain file missing"}

@app.route('/ev_remote/command', methods=['GET', 'POST'])
def remote_command():
    data = request.get_json() or {}
    command = data.get("command", "status_check")

    # Save command to EV Vault
    with open(COMMAND_FILE, 'w') as f:
        json.dump(data, f, indent=4)

    # Load EV brain memory
    brain = load_brain()

    return jsonify({
        "ev_status": "online",
        "received_command": command,
        "brain_link": brain,
        "vault_path": COMMAND_FILE
    })

@app.route('/ev_remote/result', methods=['GET'])
def get_response():
    if os.path.exists(RESPONSE_FILE):
        with open(RESPONSE_FILE, 'r') as f:
            result = json.load(f)
        return jsonify(result)
    return jsonify({'status': 'No result yet.'})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050, debug=True)
