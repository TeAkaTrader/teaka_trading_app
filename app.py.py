from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_cors import CORS
from datetime import timedelta
import os
from alert_routes import alert_bp
app.register_blueprint(alert_bp)

app = Flask(ev_remote_server)
CORS(app)

# Environment config (override with .env later)
app.config['SECRET_KEY'] = 'super-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:EVBot-80@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'jwt-super-secret'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(50), default="user")  # roles: dev, admin, user

# Routes
@app.route("/register", methods=["POST"])
def register():
    data = request.json
    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"msg": "Email already registered"}), 409
    hashed_pw = bcrypt.generate_password_hash(data["password"]).decode("utf-8")
    user = User(email=data["email"], password=hashed_pw)
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg": "User created"}), 201

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(email=data["email"]).first()
    if not user or not bcrypt.check_password_hash(user.password, data["password"]):
        return jsonify({"msg": "Bad credentials"}), 401
    token = create_access_token(identity={"email": user.email, "role": user.role})
    return jsonify({"token": token})

@app.route("/me", methods=["GET"])
@jwt_required()
def me():
    identity = get_jwt_identity()
    return jsonify(identity)

if __name__ == "__main__":
    app.run(debug=True)
