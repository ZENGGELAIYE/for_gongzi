# 第一步，先对数据库进行读取操作
from pymysql import Connection
conn = Connection(
    host= "localhost",
    port= 3306,
    user= "root",
    password= "123456"
)
# 获取游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("py_sql")
# 读取
cursor.execute("select * from orders")
result = cursor.fetchall()
f = open('练习.txt',mode="a",encoding="utf-8")
for i in result:
    dic = {}
    dic["data"] = str(i[0])
    dic["order_id"] = i[1]
    dic["money"] = i[2]
    dic["province"] = i[3]
    dic["data"] = dic["data"].replace("datetime.date","")
    f.write(str(dic) + "\n")
f.close()
conn.close()