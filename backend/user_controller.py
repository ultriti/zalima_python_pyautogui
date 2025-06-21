from flask import Blueprint, request, session, jsonify
import bcrypt
from database import get_db

db = get_db()
# user_bp = Blueprint('user', __name__)



# @user_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    user = db.user_register.find_one({'email': email})
    if not user:
        return jsonify({'error': 'Invalid email or password'}), 401

    if bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
        session["user_id"] = str(user['_id'])
        return jsonify({'message': 'Login successful', 'user': str(user['_id'])}), 200
    else:
        return jsonify({"error": "Invalid password"}), 401

# @user_bp.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Logged out successfully'}), 200

# @user_bp.route('/home', methods=['GET'])
def home():
    if "user_id" in session:
        user_id = session.get("user_id")
        user = db.user_register.find_one({'_id': user_id})
        if user:
            return jsonify({'user': {'username': user['username'], 'email': user['email']}}), 200

    return jsonify({'error': 'User not logged in'}), 401
