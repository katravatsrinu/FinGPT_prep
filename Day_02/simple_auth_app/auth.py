from flask import Blueprint, request, jsonify
import jwt
import datetime

auth_bp = Blueprint('auth', __name__)
SECRET_KEY = 'mysecretkey'

# In-memory user store
users = []

# REGISTER
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']
    role = data.get('role', 'user')  # default role: user

    for user in users:
        if user['username'] == username:
            return jsonify({'message': 'User already exists'}), 400

    users.append({'username': username, 'password': password, 'role': role})
    return jsonify({'message': 'User registered successfully'})


# LOGIN
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    user = next((u for u in users if u['username'] == username and u['password'] == password), None)

    if not user:
        return jsonify({'message': 'Invalid credentials'}), 401

    # Create JWT
    token = jwt.encode({
        'username': user['username'],
        'role': user['role'],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, SECRET_KEY, algorithm='HS256')

    return jsonify({'token': token})
