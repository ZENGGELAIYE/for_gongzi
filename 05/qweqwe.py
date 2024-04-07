# datetime 年月日，时分秒
# date 年月日
# time 时分秒

from datetime import datetime
from datetime import date
# print(datetime.now()) # 打印现在是几点
# print(datetime(2022,1,30,12,1)) #吧这种时间换成标准时间模式
# t1 = datetime(2022,1,16,12,1)
# t2 = datetime(2022,1,30,13,1)
# diff = t2 - t1
# print(diff.total_seconds()) # 一共经过了多少秒钟
#
# # 时间转化为字符
# t = datetime(2022,1,30,13,1)
# print(t.strftime("今天是%Y年%m月%d日%H时%M分%S秒"))

# # 字符转化为时间
# s1 = input("请输入第一个时间(YYYY-mm-dd HH:MM:SS):")
# s2 = input("请输入第二个时间(YYYY-mm-dd HH:MM:SS):")
#
# t1 =datetime.strptime(s1, "%Y-%m-%d %H:%M:%S") #p:parse
# t2 =datetime.strptime(s2, "%Y-%m-%d %H:%M:%S")
#
# print(t2-t1)

# date
print(date.today())
# date也可以进行strftime和strptime操作
print(date(1998, 1, 2).strftime("%Y年，%m月，%d日"))

s = input("输入今天的时间：")
m = date.strptime(s, "%Y,%m,%d") # 这个不行呢
print(m)