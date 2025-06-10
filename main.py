
import requests

base_url = "http://127.0.0.1:5000"

def register():
    res = requests.post(f"{base_url}/register", json={
        "email": "alpha@teaka.ai",
        "password": "Starforge123"
    })
    print("📝 Register:", res.status_code, res.json() if res.headers.get('Content-Type') == 'application/json' else res.text)
    return res

def login():
    res = requests.post(f"{base_url}/login", json={
        "email": "alpha@teaka.ai",
        "password": "Starforge123"
    })
    print("🔐 Login:", res.status_code, res.json() if res.headers.get('Content-Type') == 'application/json' else res.text)
    return res.json().get("token") if res.status_code == 200 else None

def get_me(token):
    headers = {"Authorization": f"Bearer {token}"}
    res = requests.get(f"{base_url}/me", headers=headers)
    print("👤 Me:", res.status_code, res.json() if res.headers.get('Content-Type') == 'application/json' else res.text)

if __name__ == "__main__":
    register()
    token = login()
    if token:
        get_me(token)
    else:
        print("❌ Login failed. No token received.")
