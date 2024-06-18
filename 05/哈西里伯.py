import hashlib
# # 创建md5对象
# obj = hashlib.md5()
# # 要把加密的信息传递给obj
# obj.update("666666".encode("utf-8"))
# # 从obj中拿到密文
# mi = obj.hexdigest() # hexdigest十六进制
# print(mi) # f379eaf3c831b04de153469d1bec345e
#
# # 正常的默认加密过程很容易撞库的
# # 解决办法--加盐
# obj = hashlib.md5(b'asdasddzxc') # b'这个中间就是加的盐'只允许是asc码
# obj.update("666666".encode("utf-8"))
# print(obj.hexdigest())

# 用户注册
# def jiami(salt,password):
#     obj = hashlib.md5(salt)
#     obj.update(password.encode("utf-8"))
#     return obj.hexdigest()
# username = input("请输入你的用户名：")
# password = input("请输入你的密码：")
# mi_password = jiami(username.encode('utf-8'),password)
# f = open("mima.txt",mode="w",encoding="utf-8")
# f.write(username)
# f.write("\n")
# f.write(mi_password)

# 登录
# a = True
# while a:
#     usn = input("请输入你的用户名：")
#     psd = input("请输入你的密码：")
#     def jiami(usn,psd):
#         obj = hashlib.md5(usn)
#         obj.update(psd.encode("utf-8"))
#         return obj.hexdigest()
#     mi_psd = jiami(usn.encode('utf-8'),psd)
#     f = open('mima.txt',mode="r",encoding="utf-8")
#     line1 = f.readline().strip() # 必须要加这个strip去除空额
#     line2 = f.readline().strip() # 切记要加这个strip
#     if usn == line1 and mi_psd == line2:
#         print("登陆成功")
#         a = False
#     else:
#         print("登陆失败")

# 文件也可以加密
# obj = hashlib.md5(b'sadasxz')
# f = open("wangfeng.txt",mode="rb") # 这里的rb是把文件当作字节来读取的，不必再encode。
# for line in f:
#     obj.update(line) # 由于已经把文件当作字节来读取了，所以不必再其进行encode了
# print(obj.hexdigest())

obj = hashlib.md5(b'sadasxz')
f = open("wangfeng.txt",mode="r",encoding='utf-8')
for line in f:
    obj.update(line.encode('utf-8'))
print(obj.hexdigest())
