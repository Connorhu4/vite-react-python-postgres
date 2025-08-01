from models.user import User
from utils.db import db_session
from utils.hash import hash_password, verify_password

def register_user(username, password):
    with db_session() as db:  # 使用上下文管理器
        if db.query(User).filter_by(username=username).first():
            return {"message": f"用户名 '{username}' 已被注册！"}, 400
        hashed_password = hash_password(password)
        user = User(username=username, password=hashed_password)
        db.add(user)
        db.commit()
        return {"message": f"用户 '{username}' 注册成功！"}, 201
    pass

def login_user(username, password):
    with db_session() as db:  # 使用上下文管理器
        user = db.query(User).filter_by(username=username).first()
        if user and verify_password(password, user.password):
            return {"message": f"欢迎回来，{username}！登录成功！"}, 200
        return {"message": "用户名或密码错误！"}, 401
    pass