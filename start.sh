#!/bin/bash

if [ "$1" == "stop" ]; then
    echo "停止 Flask 服务端..."
    pkill -f "python3 app.py" && echo "Flask 服务端已停止！"

    echo "停止 PostgreSQL 数据库..."
    brew services stop postgresql && echo "PostgreSQL 数据库已停止！"
    exit 0
fi

# 启动 PostgreSQL 数据库
echo "启动 PostgreSQL 数据库..."
brew services start postgresql
if [ $? -eq 0 ]; then
    echo "PostgreSQL 数据库启动成功！"
else
    echo "PostgreSQL 数据库启动失败，请检查服务状态！"
    exit 1
fi

# 启动 Flask 服务端
echo "启动 Flask 服务端..."
cd backend || { echo "backend 目录不存在"; exit 1; }

python3 app.py &  # 将 Flask 服务端放入后台运行
if [ $? -eq 0 ]; then
    echo "Flask 服务端启动成功！"
else
    echo "Flask 服务端启动失败，请检查代码或环境配置！"
    exit 1
fi

# 启动 React 前端
echo "启动 Web 前端..."
cd ../web || { echo "web 目录不存在"; exit 1; }
# 在新终端窗口中启动 React 前端
open -a Terminal "`pwd`" && sleep 2
osascript -e 'tell application "Terminal" to do script "cd \"'$(pwd)'\"; npm start" in front window'

# if npm start; then
#     echo "React 前端启动成功！"
# else
#     echo "React 前端启动失败，请检查代码或环境配置！"
#     exit 1
# fi