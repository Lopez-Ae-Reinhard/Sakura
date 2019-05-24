"""
    dict项目用于处理数据
"""
import pymysql
import hashlib


# 编写功能类,提供给服务端使用
class Database:
    def __init__(self,
                 host="localhost",
                 port=3306,
                 user="root",
                 password='123456',
                 database='dictionary_system',
                 charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        self.connect_db()
        self.create_cursor()

    # 连接数据库
    def connect_db(self):
        self.db = pymysql.connect(host=self.host,
                                  port=self.port,
                                  user=self.user,
                                  password=self.password,
                                  database=self.database,
                                  charset=self.charset)

    # 创建游标
    def create_cursor(self):
        self.cur = self.db.cursor()

    # 关闭数据库
    def close(self):
        self.cur.close()
        self.db.close()

    # 处理注册
    def register(self, name, password, email):
        sql = "select * from userinfo where user_name=%s"
        self.cur.execute(sql, [name])
        r = self.cur.fetchone()
        if r:
            return False

        # 加密处理
        hash = hashlib.md5("tiger".encode())
        hash.update(password.encode())
        sql = "insert into userinfo (user_name,password,email) values (%s,%s,%s)"
        try:
            self.cur.execute(sql, [name, hash.hexdigest(), email])
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            return False

    # 处理登录
    def login(self, name, password):
        hash = hashlib.md5("tiger".encode())
        hash.update(password.encode())
        sql = 'select * from userinfo where user_name = %s and password = %s'
        self.cur.execute(sql, [name, hash.hexdigest()])
        one_row = self.cur.fetchone()
        if one_row:
            return True
        else:
            return False

    # 插入历史记录
    def insert_history(self, name, word):
        sql = "insert into history (user_name,information) values (%s, %s)"
        try:
            self.cur.execute(sql, [name, word])
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print(e)

    # 查询单词
    def query(self, word):
        sql = "select explanation from dictionary where word = %s"
        self.cur.execute(sql, [word])
        r = self.cur.fetchone()
        if r:
            return r[0]
        else:
            return None

    # 查询历史记录
    def find_record(self, name):
        sql = "select * from history where user_name = %s order by id desc limit 10"
        self.cur.execute(sql, [name])
        r = self.cur.fetchall()
        history = []
        if r:
            for i in r:
                msg = "%s 查询单词: %s 时间 %s" % (i[1], i[2], i[3])
                history.append(msg)
            return history
        else:
            return None
