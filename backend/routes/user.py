from flask import Blueprint, request, jsonify
from services.auth_service import register_user, login_user

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({"message": "用户名和密码不能为空"}), 400
    return register_user(username, password)

@bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({"message": "用户名和密码不能为空"}), 400
    return login_user(username, password)