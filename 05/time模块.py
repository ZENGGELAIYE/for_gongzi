# time模块可以控制程序执行的频率 time.sleep
import time
import random
# while 1:
#     print("抓取百度的信息")
#     time.sleep(random.randint(1,5)) # 让程序在这儿睡眠一段时间后再执行



# print(time.time()) # 1712407290.028699   这个数字代表的是一个时间戳
# 代表从某个时间点到现在过了多少秒
# 可以用来计算时间

start = time.time()
for i in range(1000000):
    print(i)
end = time.time()
print(start - end) # 计算上面那个程序执行所消耗的时间