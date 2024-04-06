# name = input("你叫什么名字：")
# age = input("你多少岁：")
# adress = input("你住在哪里：")
# hobby = input("你喜欢干什么：")
# s = "我叫%s, 我%s岁， 我住在%s, 我喜欢%s" % (name,age,adress,hobby)
# s1 = "我叫,我{}岁，我住在{},我喜欢{}".format(name,age,adress,hobby)
# s0 = f"我叫{name},我{age}岁，我住在{adress},我喜欢{hobby}"
# print(s1)

# # 切片
# s = "我是李艺洁的老汉"
# # print(s[0:4])
# print(s[-1:-6:-1])

# verify_code = "sB1s"
# user_put = input(f"输入验证码({verify_code}):")
# if verify_code.upper() == user_put.upper():
#     print("你输入对了")
# else:
#     print("请输入正确的验证码：")

# user_name = input("请输入用户名：")
# pass_word = input("请输入密码：")
# if user_name.strip() == "niushen":
#     if pass_word.strip() == "123":
#         print("登陆成功")
#     else:
#         print("登陆失败")
# else:
#     print("登陆失败")

#replace的用法，replace一边拿用来替换空格，且必须得用新的变量来命名
# s = "   我  ZL是李 英杰 的老 豆"
# print(s.strip())
# s1 = s.replace(' ','')
# print(s1)

#split 切片操作，用什么切割就会损失什么东西,也必须得使用一个新的变量来命名
# s = "python_java_javascript_C_C++"
# a = s.split("_")
# print(a[2])

# 查找和判断
# s = "你好啊，我是赛利亚"
# s1 = s.find("赛利亚")
# s2 = s.find("傻逼")
# print(s1)
# print(s2)
# s3 = s.index("赛利")
# print(s3)
#
# user_name = input("请输入你的名字：")
# if user_name.startswith("李"):
#     print("你是李氏得后代")
# else:
#     print("你不是李氏后代")

# user_name = input("请输入你的名字：")
# if user_name[0] == "李":
#     print("你是李氏得后代")
# else:
#     print("你不是李氏后代")

# #判断输入是否为整数
# money = input("输入你有多少钱：")
# money = int(money)
# # if money.isdigit():
# #     print("你输入的是整数")
# # else:
# #     print("你输入的不是整数")
# print(money)

# a = input("请输入你想说的话：")
# b = len(a)
# print(f"你输入的话得长度为{b}")

# a = ["李英杰","shi","dashabi"]
# b = "".join(a)
# print(b)