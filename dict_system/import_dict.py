import pymysql
import re

db = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password='123456',
    database='dictionary_system',
    charset='utf8'
)
cur = db.cursor()

dict_txt = open("dict.txt", 'r')
while True:
    row = dict_txt.readline()
    if not row:
        break
    tup = re.findall(r"(\w+)\s+(.*)", row)[0]
    word = tup[0]
    explanation = tup[1]
    sql = "insert into dictionary (word,explanation) values (%s,%s);"
    try:
        cur.execute(sql, [word, explanation])
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
