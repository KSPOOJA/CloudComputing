from flask import Blueprint, request, jsonify
from extensions import db
from models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from services.email_service import send_email

bp = Blueprint('auth_routes', __name__, url_prefix='/auth')

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data['email']
    password = data['password']
    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({'message': 'User already exists'}), 400
    new_user = User(email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered'}), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        login_user(user)
        send_email('Login Alert', user.email, 'You have successfully logged in.')
        return jsonify({'message': 'Logged in'}), 200
    return jsonify({'message': 'Invalid credentials'}), 400

@bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logged out'}), 200
