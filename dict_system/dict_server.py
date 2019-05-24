"""
    dict服务端
    处理请求逻辑
"""

from socket import *
from multiprocessing import Process
import signal
import sys
from time import sleep
from dict_db import *

# 全局变量
HOST = "0.0.0.0"
PORT = 14190
ADDR = (HOST, PORT)


# 网络连接
def main():
    # 创建数据库连接对象
    db = Database()

    # 创建套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)

    # 处理僵尸进程
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)

    # 等待客户端的链接
    print("监听端口14190")
    while True:
        try:
            c, addr = s.accept()
            print("链接来自", addr)
        except KeyboardInterrupt:
            s.close()
            db.close()
            sys.exit("服务器退出")
        except Exception as e:
            print(e)
            continue

        # 创建子进程
        p = Process(target=do_request, args=(c, db))
        # 父进程停止,子进程也停止
        p.daemon = True
        p.start()


# 处理请求
def do_request(c, db):
    # 生成游标 db.cur
    db.create_cursor()
    while True:
        data = c.recv(1024).decode()
        if not data or data[0] == "Exit":
            c.close()
            sys.exit("客户端退出")
        elif data[0] == "R":
            do_register(c, db, data)
        elif data[0] == "L":
            do_login(c, db, data)
        elif data[0] == "Q":
            do_query(c, db, data)
        elif data[0] == "H":
            do_record(c, db, data)


# 注册操作
def do_register(c, db, data):
    tmp = data.split(" ")
    name = tmp[1]
    password = tmp[2]
    email = tmp[3]
    if db.register(name, password, email):
        c.send(b"PASS")
    else:
        c.send(b"Error")


# 登录操作
def do_login(c, db, data):
    tmp = data.split(" ")
    name = tmp[1]
    password = tmp[2]
    if db.login(name, password):
        c.send(b"PASS")
    else:
        c.send(b"Error")


# 查询操作
def do_query(c, db, data):
    tmp = data.split(" ")
    name = tmp[1]
    word = tmp[2]

    # 插入历史记录
    db.insert_history(name, word)

    # 查单词 没查到返回None
    mean = db.query(word)
    if not mean:
        c.send("没有查到该单词".encode())
    else:
        msg = "%s的解释为: %s" % (word, mean)
        c.send(msg.encode())

# 查询历史记录
def do_record(c, db, data):
    name = data.split(" ")[1]
    # 查询
    mean = db.find_record(name)
    # 查询到
    if not mean:
        c.send(b"Error")
        return
    else:
        c.send(b"PASS")
        for i in mean:
            sleep(0.1)
            c.send(i.encode())
        sleep(0.1)
        c.send("##".encode())


if __name__ == "__main__":
    main()
