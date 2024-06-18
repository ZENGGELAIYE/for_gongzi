import os
# 所有和系统相关的操作都在os模块里面
# 1. 创建文件夹
# def func():
#     for i in range(10):
#         name = i
#         os.makedirs(f'C:/dadada/{name}')
# func()

a = os.path.split('C:/dadada/1')
print(a)