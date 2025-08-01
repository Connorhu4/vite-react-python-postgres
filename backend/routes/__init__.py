from .user import bp as user_bp

# 创建一个蓝图集合
def register_routes(app):
    """
    注册所有蓝图到 Flask 应用
    """
    app.register_blueprint(user_bp, url_prefix='/auth')
