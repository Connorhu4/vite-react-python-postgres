import sqlite3

# 初始化数据库
def init_db():
    conn = sqlite3.connect("database.db")  # 连接数据库（如果不存在会自动创建）
    cursor = conn.cursor()
    # 创建 tasks 表（如果不存在）
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            status TEXT DEFAULT 'pending'
        )
    """)
    conn.commit()
    conn.close()

# 添加任务
def add_task(task):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()
    conn.close()
    print(f"任务 '{task}' 已添加！")

# 查看任务
def view_tasks():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, task, status FROM tasks")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("\n当前没有任务！")
    else:
        print("\n当前任务列表：")
        for row in rows:
            print(f"{row[0]}. {row[1]} [{row[2]}]")

# 删除任务
def delete_task(task_id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    print(f"任务 ID {task_id} 已删除！")

# 更新任务状态
def update_task_status(task_id, status):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, task_id))
    conn.commit()
    conn.close()
    print(f"任务 ID {task_id} 状态已更新为 '{status}'！")

# 显示菜单
def show_menu():
    print("\n=== To-Do List ===")
    print("1. 查看任务")
    print("2. 添加任务")
    print("3. 删除任务")
    print("4. 更新任务状态")
    print("5. 退出")

# 主程序逻辑
def main():
    init_db()  # 初始化数据库
    while True:
        show_menu()
        choice = input("\n请选择操作（1-5）： ")
        if choice == "1":
            view_tasks()
        elif choice == "2":
            task = input("\n请输入要添加的任务： ")
            if task.strip():
                add_task(task)
            else:
                print("任务不能为空！")
        elif choice == "3":
            view_tasks()
            try:
                task_id = int(input("\n请输入要删除的任务 ID： "))
                delete_task(task_id)
            except ValueError:
                print("请输入有效的任务 ID！")
        elif choice == "4":
            view_tasks()
            try:
                task_id = int(input("\n请输入要更新状态的任务 ID： "))
                status = input("请输入新的状态（pending/done）： ").strip().lower()
                if status in ["pending", "done"]:
                    update_task_status(task_id, status)
                else:
                    print("状态只能是 'pending' 或 'done'！")
            except ValueError:
                print("请输入有效的任务 ID！")
        elif choice == "5":
            print("退出程序，再见！")
            break
        else:
            print("无效的选择，请重新输入！")

# 程序入口
if __name__ == "__main__":
    main()