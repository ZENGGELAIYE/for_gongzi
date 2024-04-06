"""
1.找到这个文件，然后打开它
open(文件路劲，mode = “”， encoding = “”)
文件路径：
    1.绝对路径
        d:/test/****.txt
    2.相对路劲
        相对于你的程序所在的文件夹
        ../   返回上一级
mode:
    r: read 读取文件
    w： write 写
    a: append 追加写入
    b: 读写的是非文本文件 -> bytes
with: 上下文  不需要手动的去关闭掉一个文件
"""

# f = open("../01/日本激情.txt", mode = "r",encoding="utf-8")
# content = f.read()  # 这个是全部读取
# print(content)

# content = f.readline()  # 这个操作是只读取一行
# print(content)
#
# content = f.readline().strip() # 为了删除TXT文件右侧的换行符
# print(content)
#
# content = f.readline()
# print(content)
#
# content = f.readlines() # 读取所有内容，并且存到列表中
# print(content)

# # 最重要的一种文本读取方师。
# f = open("../01/日本激情.txt", mode = "r",encoding="utf-8")
# for line in f:
#     print(line.strip())

# # 写入文件
# # w模式下，如果文件不存在，自动创建一个文件
# # w模式下，每一次open都会清空掉文件中的内容
# f = open("嫩模", mode="w", encoding="utf-8")
# f.write("baby")
# # 准备一个列表，吧列表的每一项内容，写入到文件当中
# lst = ["奥特曼","诺手","迪迦","大哥大"]
# f = open("奥特曼大合集",mode="w",encoding="utf-8")
# for item in lst:
#     f.write(item+"\n")
# f.close() # 不加这个东西后续就无法读取（关闭当前的文件操作）
# s = open("奥特曼大合集",mode="r",encoding="utf-8")
# print(s.read())

# # a模式 直接添加，不会清空文件
# f = open("奥特曼大合集",mode="a",encoding="utf-8")
# f.write("你好牛逼")
# f.close()
# f = open("奥特曼大合集",mode="r",encoding="utf-8")
# print(f.read())
#
# # with
# with open("奥特曼大合集",mode="r",encoding="utf-8") as f:
#     for item in f:
#         print(item.strip())
# # f.read()  # 在with操作之外再对文件进行操作会报错，这是因为with操作执行完之后会自动关闭文件

# # 想要读取图片
# # 读取非文本文件的时候要加上b
# with open("发展图.jpg",mode="rb") as f:
#     for item in f:
#         print(item)


# 文件的复制：
# 从源文件中读取内容，写入到新的文件中去
# with (open("发展图.jpg",mode="rb") as f ,# pycharm这个版本已经可以回车不报错了，如果报错的话可以加个/
#       open("../01/大傻逼.jpg",mode="wb") as f2):
#     for item in f:
#         f2.write(item)


import os # 和操作系统相关的模块引入
import time # 和时间相关的模块导入
# 文件修改 把姓大的改成姓小的
with (open("奥特曼大合集",mode="r",encoding="utf-8") as s,
      open("123.txt",mode="w",encoding="utf-8") as n):
    for item in s:
        item = item.strip() # 去掉空格,!!!!!字符串必须重新赋值，不然不会发生改变
        if item.startswith("大"):
            # item = item.replace("大","小") # 另一种修改方式
            item = "小" + item[1:]
        item = item + "\n"
        n.write(item)
time.sleep(5)  # 让程序休眠3秒
# 删除原文件
os.remove("奥特曼大合集")
time.sleep(5)
# 文件重命名
os.rename("123.txt","奥特曼大合集")
