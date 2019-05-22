"""
    ftp文件服务器思路分析
    1. 技术点分析

        * 并发模型  多线程并发模式
        * 数据传输  TCP传输

    2. 结构设计

        * 客户端发起请求,打印请求提示界面
        * 文件传输功能封装为类

    3. 功能分析

        * 网络搭建
        * 查看文件库信息
        * 下载文件
        * 上传文件
        * 客户端退出

    4. 协议
        L 表示请求文件列表
        Q 表示退出
        G 表示下载
"""
from threading import Thread
from socket import *
from time import sleep
import sys
import os

# 全局变量
HOST = "0.0.0.0"
PORT = 14190
ADDR = (HOST, PORT)
FTP = "/home/tarena/FTP/"


# 将请求功能封装为类
class FtpServer:
    def __init__(self, connfd, FTP_PATH):
        self.connfd = connfd
        self.FTP_PATH = FTP_PATH

    def do_list(self):
        # 获取文件列表
        files = os.listdir(self.FTP_PATH)
        if not files:
            self.connfd.send("该文件类型为空".encode())
            return
        else:
            self.connfd.send(b"copy")
            sleep(0.1)

        fs = ""
        for file in files:
            if file[0] != "." and \
                    os.path.isfile(self.FTP_PATH + file):
                fs += file + "\n"
        self.connfd.send(fs.encode())

    def do_get(self, filename):
        try:
            fd = open(self.FTP_PATH + filename, "rb")
        except Exception:
            self.connfd.send("文件不存在".encode())
            return
        else:
            self.connfd.send(b"copy")
            sleep(0.1)
        while True:
            data = fd.read(1024)
            if not data:
                sleep(0.1)
                self.connfd.send(b"##")
                break
            self.connfd.send(data)

    def do_put(self, filename):
        if os.path.exists(self.FTP_PATH + filename):
            self.connfd.send("该文件已存在")
            return
        else:
            self.connfd.send(b"copy")
        fd = open(self.FTP_PATH + filename, "wb")
        sleep(0.1)
        while True:
            data = self.connfd.recv(1024)
            if data == b"##":
                break
            fd.write(data)
        fd.close()


# 客户端请求处理函数
def handle(connfd):
    cls = connfd.recv(1024).decode()
    FTP_PATH = FTP + cls + "/"
    ftp = FtpServer(connfd, FTP_PATH)
    while True:
        print(FTP_PATH)
        # 接受客户端的请求
        data = connfd.recv(1024).decode()
        # 如果客户端断开返回data为空
        if not data or data[0] == "Q":
            return
        elif data[0] == "L":
            ftp.do_list()
        elif data[0] == "G":
            filename = data.split(" ")[-1]
            ftp.do_get(filename)
        elif data[0] == "P":
            filename01 = data.split(" ")[-1]
            ftp.do_put(filename01)


def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(ADDR)
    sockfd.listen(9)
    print("正在监听端口 14190...")
    while True:
        try:
            connfd, addr = sockfd.accept()
        except KeyboardInterrupt:
            print("退出服务程序")
            sys.exit()
        except Exception as e:
            print(e)
            continue
        print("链接的客户端:", addr)
        client = Thread(target=handle, args=(connfd,))
        client.setDaemon(True)
        client.start()


if __name__ == "__main__":
    main()
