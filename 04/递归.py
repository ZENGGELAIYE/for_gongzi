# # 三元表达式
# a = 10
# b = 20
# if a > b:
#     print(a)
# else:
#     print(b)
# print(a if a > b else b) # 这个就叫三元表达式，和上面的if,else是一样的

# 递归的本质就是自己调用自己
# import os
# def read(path,ceng): # path 指的是文件的路劲
#     lst = os.listdir(path) # 用来遍历文件夹
#     for name in lst:
#         # 需要拼接出正确的文件路劲
#         real_path = os.path.join(path, name) # c:\test\a.txt
#         if os.path.isdir(real_path): # 判断其是否为一个目录
#             print(ceng*"\t"+name)
#             read(real_path,ceng+1)
#         else:
#             print(name)
# read("../../Python_project",1)

# 汉诺塔
# 将n-1层铁饼，从A经过C移动到B。
# 然后将A铁饼移动到C
# 最后将铁饼，从B经过A移动到C

# def honio(n, a, b, c):
#     if n > 0:
#         honio(n-1,a, c, b)
#         print(f"{a}移动到{c}")
#         honio(n-1,b, a, c)
# honio(2,"A","B","C")

