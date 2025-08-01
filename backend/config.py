import os
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

# 获取环境变量
database_url = os.getenv('DATABASE_URL', 'postgresql://postgres:password@localhost:5432/defaultdb')
secret_key = os.getenv('SECRET_KEY', 'defaultsecretkey')

print(f"Database URL: {database_url}")
print(f"Secret Key: {secret_key}")