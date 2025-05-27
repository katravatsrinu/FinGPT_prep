import requests

data = {
    "name": "Srinu",
    "role": "FinanceGPT Developer"
}

response = requests.post("https://httpbin.org/post", json=data)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
from flask import Blueprint, request, jsonify
import jwt

protected_bp = Blueprint('protected', __name__)
SECRET_KEY = 'mysecretkey'


def verify_token(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except:
        return None


# PROTECTED route (any logged-in user)
@protected_bp.route('/profile')
def profile():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'message': 'Token missing'}), 403

    user_data = verify_token(token)
    if not user_data:
        return jsonify({'message': 'Invalid or expired token'}), 403

    return jsonify({'message': f"Welcome {user_data['username']}!", 'role': user_data['role']})


# ADMIN-only route
@protected_bp.route('/admin')
def admin():
    token = request.headers.get('Authorization')
    user_data = verify_token(token)

    if not user_data or user_data['role'] != 'admin':
        return jsonify({'message': 'Admin access required'}), 403

    return jsonify({'message': 'Welcome Admin! 🎉'})
