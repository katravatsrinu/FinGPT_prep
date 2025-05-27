from flask import Blueprint, request, jsonify
import jwt

protected_bp = Blueprint('protected', __name__)
SECRET_KEY = 'mysecretkey'


def verify_token(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except:
        return None
    
# protected_