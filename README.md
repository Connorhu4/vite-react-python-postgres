# todoPython 项目说明

本项目包含前后端两部分，分别为 Flask 后端（backend）和 React 前端（web），用于实现一个简单的待办事项管理系统。

---

## 目录结构

```
todoPython/
├── backend/         # Flask 后端服务
│   ├── app.py       # 后端主程序入口
│   ├── config.py    # 后端配置文件
│   ├── routes/      # 路由相关代码
│   ├── utils/       # 工具类（如数据库操作）
│   └── ...          # 其他后端文件
├── web/             # React 前端项目
│   ├── src/         # 前端源码
│   ├── public/      # 静态资源
│   ├── package.json # 前端依赖配置
│   └── ...          # 其他前端文件
├── .gitignore       # Git 忽略文件配置
└── README.md        # 项目说明文档
```

---

## 后端（Flask）

- 入口文件：`backend/app.py`
- 配置文件：`backend/config.py`
- 数据库初始化与连接管理：`utils/db.py`
- 支持 CORS 跨域
- 路由注册在 `routes` 目录下
- 提供基础的数据库连接测试接口

### 启动后端

```bash
cd backend
pip install -r requirements.txt
python app.py
```

默认监听端口：`5000`

---

## 前端（React）

- 目录：`web/`
- 使用 Create React App 脚手架
- 主要功能：待办事项管理页面，调用后端接口

### 启动前端

```bash
cd web
npm install
npm start
```

默认访问地址：[http://localhost:3000](http://localhost:3000)

---

## 常见问题

- **数据库连接失败**：请检查 `backend/config.py` 中的数据库配置项。
- **前后端跨域问题**：已在 Flask 后端启用 CORS，无需额外配置。
- **依赖安装失败**：请确保 Python 和 Node.js 环境已正确安装。

---

## 其他说明

- `.gitignore` 已配置常见的 node_modules、虚拟环境、环境变量等忽略规则。
- 推荐开发时前后端分别启动，接口地址可在前端 `.env` 文件中配置。

---

## 联系方式

如有问题或建议，请联系项目维护