# File: flask_api_routes.py
from flask import Flask, jsonify
import json
import os

app = Flask(__name__, template_folder="templates", static_folder="public")

def load_json(path):
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return {}

@app.route('/api/portfolio')
def portfolio():
    status = load_json("strategy_status.json")
    trades = load_json("trades_history.json")
    balance = 5000 + sum(t.get("pnl", 0) for t in trades)
    return jsonify({
        "balance": round(balance, 2),
        "open_trades": len([t for t in trades if t.get("open", False)]),
        "total_pnl": round(sum(t.get("pnl", 0) for t in trades), 2)
    })

@app.route('/api/history')
def history():
    trades = load_json("trades_history.json")
    return jsonify(trades)

@app.route('/api/hot_assets')
def hot_assets():
    return jsonify(load_json("hot_assets.json"))

@app.route('/api/bots')
def bots():
    return jsonify(load_json("strategy_status.json"))

@app.route('/api/feed')
def feed():
    trades = load_json("trades_history.json")
    return jsonify([{ "time": t.get("timestamp"), "symbol": t.get("symbol"), "pnl": t.get("pnl") } for t in trades])

@app.route('/api/check-alert')
def check_alert():
    return jsonify({ "alert": True })

if __name__ == '__main__':
    app.run(port=5050, debug=True)
