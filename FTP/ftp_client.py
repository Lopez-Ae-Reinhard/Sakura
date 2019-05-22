from socket import *
import sys
from time import sleep


# 具体功能
class FtpClient:
    def __init__(self, sockfd):
        self.sockfd = sockfd

    def do_list(self):
        # 发送请求
        self.sockfd.send(b"L")

        # 等待回复
        data = self.sockfd.recv(128).decode()
        if data == "copy":
            data = self.sockfd.recv(8192)
            print(data.decode())
        else:
            print(data)

    def do_quit(self):
        self.sockfd.send(b"Q")
        self.sockfd.close()
        sys.exit("进程退出,欢迎下次使用")

    def do_get(self, filename):
        # 发送请求
        self.sockfd.send(("G " + filename).encode())
        # 等待回复
        data = self.sockfd.recv(128).decode()
        if data == "copy":
            fd = open(filename, "wb")
            # 接收内容写入文件
            while True:
                data = self.sockfd.recv(1024)
                if data == b"##":
                    break
                fd.write(data)
            fd.close()
        else:
            print(data)

    def do_put(self, filename):
        try:
            fb = open(filename, "rb")
        except Exception:
            print("文件不存在")
        filename = filename.split("/")[-1]
        self.sockfd.send(("P " + filename).encode())
        data = self.sockfd.recv(128).decode()
        if data == "copy":
            while True:
                data = fb.read(1024)
                if not data:
                    sleep(0.1)
                    self.sockfd.send(b"##")
                    break
                self.sockfd.send(data)
            fb.close()
        else:
            print(data)


# 发起请求
def requst(sockfd):
    ftp = FtpClient(sockfd)
    while True:
        print("""
        ^^^^^^^  选项  ^^^^^^^
        ******  1.查看  ******
        ******  2.下载  ******
        ******  3.上传  ******
        ******  4.退出  ******
        ^^^^^^^^^^^^^^^^^^^^^
        """)

        cmd = input("输入命令(1-4)")
        if int(cmd) == 1:
            ftp.do_list()
        elif int(cmd) == 2:
            filename = input("下载文件名")
            ftp.do_get(filename)
        elif int(cmd) == 3:
            filename01 = input("上传文件名")
            ftp.do_put(filename01)
        elif int(cmd) == 4:
            ftp.do_quit()


# 网络连接
def main():
    ADDR = ("172.88.10.142", 14190)
    sockfd = socket()
    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print("连接服务器大失败")
        return
    else:
        print("""
        ****************
        1. data    
        2. music   
        3. picture
        ****************
        """)
        while True:
            cls = input("请输入文件种类:")
            if int(cls) > 3 or int(cls) < 1:
                print("超出范围")
            elif int(cls) == 1:
                sockfd.send("data".encode())
                requst(sockfd)
            elif int(cls) == 2:
                sockfd.send("music".encode())
                requst(sockfd)
            elif int(cls) == 3:
                sockfd.send("picture".encode())
                requst(sockfd)


main()
