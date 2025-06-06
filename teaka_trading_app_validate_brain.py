import json
import sys

path = r"E:\EV_Files\ev_virtual_brain.json"

try:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    print("✅ JSON is valid. Top‐level keys:", list(data.keys())[:5])
except Exception as e:
    print("❌ JSON parse error:", e)
    sys.exit(1)
