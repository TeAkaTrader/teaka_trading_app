# File: ev_alert_api.py
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = "AAFAf-5JT1yKg7c6gsk6p3UWYqiy249BPUc"
TELEGRAM_CHAT_ID = "123456789"  # Replace with real one

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    response = requests.post(url, json=data)
    return response.json()

@app.route("/api/alert", methods=["POST"])
def receive_alert():
    data = request.get_json()
    message = data.get("message", "No message received.")
    print(f"[ALERT RECEIVED] {message}")
    send_telegram_alert(message)
    return jsonify({"status": "sent", "message": message})

@app.route("/api/auto-exit", methods=["POST"])
def auto_exit_trigger():
    trade = request.get_json()
    asset = trade.get("asset", "Unknown")
    reason = trade.get("reason", "N/A")
    send_telegram_alert(f"⚠️ Auto-exit triggered for {asset}: {reason}")
    return jsonify({"status": "auto-exit sent", "asset": asset})

if __name__ == "__main__":
    app.run(port=5051)
