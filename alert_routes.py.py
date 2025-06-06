from flask import Blueprint, request, jsonify
import requests

alert_bp = Blueprint('alert_bp', __name__)

TELEGRAM_BOT_TOKEN = 7711152546:AAFAf-5JT1yKg7c6gsk6p3UWYqiy249BPUc
TELEGRAM_CHAT_ID = teaka_trader_bot

@alert_bp.route('/api/alert/send', methods=['POST'])
def send_alert():
    data = request.json
    message = data.get("message", "No message provided.")
    if not message:
        return jsonify({"error": "Message is required"}), 400

    url = f"https://api.telegram.org/bot7711152546:AAFAf-5JT1yKg7c6gsk6p3UWYqiy249BPUc
/sendMessage"
    payload = {
        "chat_id": teaka_trader_bot,
        "text": message
    }

    resp = requests.post(url, json=payload)
    if resp.status_code == 200:
        return jsonify({"status": "sent"})
    else:
        return jsonify({"error": resp.text}), 500
