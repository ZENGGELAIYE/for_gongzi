"""
演示python pymysql库的基本操作
"""
from pymysql import Connection
# 构建到mysql数据库链接
conn = Connection(
    host= "localhost", # 本地主机，主机名
    port= 3306,        # 端口
    user= "root",      # 账户
    password="123456",  # 密码
    autocommit= True # 自动确认
)
# 获取游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("world")
# 执行sql语句
# cursor.execute("create table test_mysql(id int);")
# 执行sql选取语句
cursor.execute("insert into student values (1,'你好',3);")
# 确认操作
conn.commit()
# 关闭连接
conn.close()