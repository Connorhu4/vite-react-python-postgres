import bcrypt

# 哈希加密密码
def hash_password(password: str) -> str:
    # 将密码加盐并加密
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

# 验证密码
def verify_password(password: str, hashed_password: str) -> bool:
    # 验证用户输入的密码是否与加密密码匹配
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))