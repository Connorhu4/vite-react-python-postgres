from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from config import database_url

Base = declarative_base()# 基类，用于声明模型
# 创建数据库引擎，连接到指定的数据库
# 注意：在实际应用中，数据库 URL 应该从配置文件或环境变量中读取，以避免硬编码。
# 这里的 database_url 应该是一个有效的 SQLAlchemy 数据库连接字符串，例如：
# database_url = "sqlite:///./test.db"  # SQLite 数据库
# 或者
# database_url = "postgresql://user:password@localhost/dbname"  # PostgreSQL 数据库
# 或者
# database_url = "mysql+pymysql://user:password@localhost/dbname"  # MySQL 数据库   
engine = create_engine(database_url, echo=True)
# echo=True 表示启用 SQLAlchemy 的日志记录功能，便于调试和查看 SQL 查询语句
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# 创建一个会话类，用于与数据库交互 
# autocommit=False 表示在每次操作后不自动提交事务
# autoflush=False 表示在查询前不自动刷新会话中的数据
# 初始化数据库


def init_db(app):
     # 确保导入所有模型
    from models.user import User # 导入 User 模型
    # from models.todo import Todo # 导入 Todo 模型
    Base.metadata.create_all(bind=engine)# 创建所有表
#如果使用 @contextmanager，你可以避免手动调用 db.close()，因为上下文管理器会自动处理资源的释放。
@contextmanager
def db_session():# 上下文管理器，用于管理数据库会话
    """
    创建一个数据库会话的上下文管理器
    使用时可以通过 with db_session() as db: 来获取一个数据库会话对象 db
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()