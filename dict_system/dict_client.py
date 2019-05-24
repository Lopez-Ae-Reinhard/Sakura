"""
    dict客户端
    发起请求,展示结果
"""
from socket import *
from getpass import getpass

HOST = "172.88.10.142"
PORT = 14190
ADDR = (HOST, PORT)
# 创建网络连接
s = socket()
s.connect(ADDR)


def main():
    while True:
        print("""
        =============
        |++欢迎使用++|
        =============
        |   1.注册   | 
        |   2.登录   |
        |   3.退出   |
        =============
        """)
        cmd = input("输入选项")
        if cmd == "1":
            do_register()
        elif cmd == "2":
            do_login()
        elif cmd == "3":
            s.send(b"Exit")
            print("谢谢使用")
            return
        else:
            print("输入错误,请重新输入")


# 注册操作
def do_register():
    while True:
        name = input("请输入用户名:")
        # password = getpass("请输入密码:")
        # password_confirm = getpass("请再次输入密码:")
        password = input("请输入密码:")
        password_confirm = input("请再次输入密码:")
        email = input("请输入邮箱:")
        if (" " in name) or (" " in password):
            print("用户名或密码中不能有空格")
            continue

        if password != password_confirm:
            print("两次密码不一致")
            continue

        msg = "R %s %s %s" % (name, password, email)
        # 发送请求
        s.send(msg.encode())
        # 接收反馈
        data = s.recv(1024).decode()
        if data == "PASS":
            print("注册成功")
            login(name)
        else:
            print("注册失败")
        return


# 登录操作
def do_login():
    name = input("请输入账号")
    password = input("请输入密码")
    msg = "L %s %s" % (name, password)
    s.send(msg.encode())
    # 接收反馈
    data = s.recv(1024).decode()
    if data == "PASS":
        print("登录成功")
        login(name)
    else:
        print("登录失败")
    return


# 二级界面
def login(name):
    while True:
        print("""
        =================
        |   1.查询单词   | 
        |   2.历史记录   |
        |   3.注　　销   |
        =================
        """)
        cmd = input("输入选项")
        if cmd == "1":
            do_query(name)
        elif cmd == "2":
            do_record(name)
        elif cmd == "3":
            return
        else:
            print("输入错误,请重新输入")


# 查单词
def do_query(name):
    while True:
        word = input("单词")
        # 如果输入##结束单词查询
        if word == "##":
            break
        msg = "Q %s %s" % (name, word)
        s.send(msg.encode())
        # 等待回复
        data = s.recv(4096).decode()
        print("结果为:", data)


# 查询历史记录
def do_record(name):
    msg = "H %s" % name
    s.send(msg.encode())
    data = s.recv(128).decode()
    if data == "PASS":
        while True:
        # 等待回复
            data = s.recv(1024).decode()
            if data == "##":
                break
            print("历史记录:", data)
    else:
        print("还没有历史记录")



if __name__ == "__main__":
    main()
