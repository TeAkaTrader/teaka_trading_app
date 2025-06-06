from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder="templates", static_folder="public")

@app.route('/')
def home():
    return "Flask server running!"

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(port=5050, debug=True)
