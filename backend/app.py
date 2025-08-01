from flask_cors import CORS
from utils.db import init_db, db_session
from flask import Flask, jsonify, Response
import json

app = Flask(__name__)# 创建 Flask 应用实例
CORS(app) # 启用 CORS，允许跨域请求

# 加载配置
app.config.from_pyfile('config.py')
# 它会把 config.py 文件中定义的所有大写变量（如 DATABASE_URL、SECRET_KEY 等）加载到 Flask 的 app.config 对象中。
# 这样你可以通过 app.config['KEY'] 的方式在应用中访问这些配置项，实现配置和代码分离，方便管理和修改。
# 这使得应用的配置更加灵活和可维护。


# 初始化数据库 
init_db(app)

# 注册路由
from routes import register_routes
register_routes(app)
from sqlalchemy import text
from utils.db import engine
@app.teardown_appcontext #  Flask 提供的一个装饰器，用于注册应用上下文销毁时自动执行的回调函数shutdown_session。
def shutdown_session(exception=None):
    # shutdown_session 函数在 Flask 应用上下文销毁时被调用，用于关闭数据库连接。
    """
    在 Flask 应用上下文销毁时关闭数据库连接
    """
    engine.dispose() # 释放数据库连接池中的所有连接
# 这将确保在应用关闭时，所有的数据库连接都被正确释放。
# 测试数据库连接
@app.route('/', methods=['GET'])
def test_db():
    try:
        with db_session() as db:
            result = db.execute(text("SELECT 1")).fetchone()
            response_data = {"message": "数据库连接成功了！", "result": result[0]}
            return Response(json.dumps(response_data, ensure_ascii=False), content_type="application/json")
    except Exception as e:
        response_data = {"message": "数据库连接失败！", "error": str(e)}
        return Response(json.dumps(response_data, ensure_ascii=False), content_type="application/json")

if __name__ == '__main__':
    app.run(debug=True, port=5000)