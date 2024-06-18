# 设计一个类完成数据的封装
# 设计一个抽象类，定义文件的读取相关功能，并使用子类实现具体功能
# 读取文件，生产数据对象
# 进行数据需求的逻辑计算(计算每一天的销售额)
# 通过pyedhart进行绘图
from file_define import File_Record,TextFileRead,Json_File_Read
from date_define import Record
from pymysql import Connection
textfileread = TextFileRead("D:/BaiduNetdiskDownload/资料/第13章资料/2011年1月销售数据.txt")
jsonfileread = Json_File_Read("D:/BaiduNetdiskDownload/资料/第13章资料/2011年2月销售数据JSON.txt")
jan_data : list[Record]= textfileread.read_data()
feb : list[Record]= jsonfileread.read_data()
# 将两个月份的数据合并为一个list来储存
all_data : list[Record]= jan_data + feb
# 创建sql对象
conn = Connection(
    host= "localhost",
    port= 3306,
    user= "root",
    password= "123456",
    autocommit= True
)
# 获得游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("py_sql")
# 插入数据
for record in all_data:
    sql = (f"insert into orders(order_date, order_id, money, province) "
           f"values('{record.date}', '{record.order_id}',{record.money}, '{record.province}')")
    cursor.execute(sql)
conn.close()