# # bin oct hex
# a = 18
# print(bin(a)) # 二进制
# print(oct(a)) # 八进制
# print(hex(a)) # 十六进制
# b = 0b01101
# c = 0o02210
# d = 0x12345
# print(int(b))
# print(int(c))
# print(int(d))
import random

# # sum, max, min, pow
# a = 10
# b = 3
# print(pow(a, b)) # = print(a ** b) pow是次幂的意思
# lst = [1,2222,333,12,3214,1]
# print(max(lst)) # 最大
# print(min(lst)) # 最小
# print(sum(lst)) # 求和
# lst.sort() # 必须这样，不能用个函数替换
# print(lst)


# # list
# s = {1,2,3,} # tuple 元组
# # lst = []
# # for item in s:
# #     lst.append(item)
# lst = list(s) # 默认列表操作里面有一个for循环
# print(lst)

# # slice
# s = slice(1,6,2) # 切片，从一到六隔两个切一刀
# print("你是傻逼吗你，我去你妈的"[s])

# format, ord, chr
# format 格式化
# a = 18
# print(format(a,"08b")) # b(bin):二进制，o(oct)八进制, x(hex)十六进制
# print(format(a,"08o"))
# print(format(a,"08x"))

# ord chr
# a = "中"  # python的内存中使用的是Unicode
# print(ord(a)) # 中在Unicode中的编码位是20013
# print(chr(20013)) # 给出编码的位置显示出编码为所在的内容
# for i in range(65536):
#     print(chr(i)+" ",end = "") # end等于空表示不要换行

# enumerate, all, any
# print(all([1, "ni", "你好"]))  # 当成and来看 t and t and t为真
# print(all([0, "你好", "在吗"])) # f and t and t 为假
# print(any([1, "", 0])) # any当成or来看 t or f or f为真
# print(any([0, "", 0])) # f or f or f为假

# enumerate
# lst = ["张祖涛", "张无忌", "答辩下", "诺克萨斯之手"]
# for item in enumerate(lst): # enumerate出来的东西是一个元组
#     print(item)
# for index, item in enumerate(lst): # enumerate出来的东西是一个元组
#     print(index, item)
# for i in range(len(lst)):
#     print(i, lst[int(i)])

# hash  id
# a = "呵呵"
# print(hash(a)) # 一定是一个数字 -> 想办法转化为内存地址。然后进行数据的存储 -> 字典（集合）哈希表
# # 每次计算的hash值都不一样，但是并不妨碍其正常运行
# print(id(a)) # 就直接是一个地址id
#
# # help
# print(help(print)) # 对函数进行解释
# # dir
# s = "呵呵"
# print(dir(s)) # 告诉你当前可以对其进行什么操作

# # iter next
# lst = [111, 222, 333, 444]
# # it = lst.__iter__()
# it = iter(lst)
# # it.__next__()
# print(next(it))
# print(next(it))
# print(next(it))

# callable:判断xx是否可以被调用（调用就是是否可以在其后面添加括号）
# def func():
#     pass
# print(callable(func))
# print(callable(123))

# def run():
#     print("哥们可以跑")
# def jump():
#     print("哥们也可以跳")
# def fn(obj):
#     if callable(obj) == True:
#         obj()
#     else:
#         print("您输入有误！！！")
# fn(run)
# fn(jump)
# fn(123) # 不可以被调用的话就会报错
#
# # __import__() 动态加载一个模块
# func = input("请输入函数：")
# __import__(func)
# print(random.randint(1, 4))

# 字符串的执行
# s = "1 + 1 "
# ret = eval(s) # 可以把字符串当作代码来执行，有返回值
# print(ret)

# s = "a = 100"
# exec(s) # 没有返回值
# print(a) # pycharm报错，程序不一定有问题

# compile() 把一段代码加载。后面可以通过exec和eval来执行
# compile(执行的代码，文件名(有代码的时候就不用输入文件名)，执行的方式(exec, eval, single))
# s = compile("for i in range(10): print(i)", "", "exec")
# exec(s)
#
# s1 = compile("1 + 1", "", "eval")
# r = eval(s1)
# print(r)
#
# s2 = compile("n = int(input('请输入内容:'))","","single")
# r = eval(s2)
# print(n)
#
# s = '["阿斯顿", "丹斯", "按时到场"]'
# r = eval(s)
# print(r, type(r))

# # dict
# d = dict([("赵本山","马大帅"),("范围","范德彪")])
# print(d)

# # list -> tuple
# # set -> frozenset
# s = frozenset((11,22,11,333))
# print(s)
# # 不可以加东西

# # zip 拉链函数
# lst1 = ["赵本山", "周杰伦", "范冰冰"]
# lst2 = ["马大帅", "灌篮高手", "情深深雨蒙蒙"]
# lst3 = ["马大帅", "伦伦", "小燕子"]
# a = zip(lst1,lst2,lst3) # zip具有水桶效应，只接受最短的。
# print("__iter__" in dir(a)) # 判断其是否可以进行迭代
# for item in a:
#     print(item)

# lst1 = ["赵本山", "周杰伦", "范冰冰"]
# lst2 = ["马大帅", "灌篮高手", "情深深雨蒙蒙"]
# a = dict(zip(lst1,lst2))
# print(a)
#
# # reversed
# lst1 = ["赵本山", "周杰伦", "范冰冰"]
# s = reversed(lst1) # 翻转列表生成一个迭代器
# print(s)
# print(list(s)) # 用list把这个列表拿空
#
# # slice
# scentence = "我好想回家去宜宾啊！"
# new_scentence = "好想回家洗澡烧烤，使劲耍啊"
# ss = slice(1, 6, 2) # 提前定义好一个切片，想用的时候直接拿
# print(scentence[ss]) # 想改的时候也可以一次性就改完
# print(new_scentence[ss])

# # ord 和 chr
# print(ord("国")) # c:charactor 字符
# print(chr(22269))
# # 可以用来生成验证码
# import random
# n = random.randint(65, 92)
# print(chr(n))

# # repr: 一个字符串最应该表现得方式
# print(str("你好呀，我叫\t周杰伦！"))
# print(repr("你好呀，我叫\t周杰伦")) # 说人话：就是带了个引号，看起来没有执行\T但是会执行。
#
# # r字符串 和repr没有关系
# print(r"你好呀，我叫\t周\n杰伦！") # 字符串里面的所有操作都不会被执行
#
# a = 48
# print(format(a,"08d")) # 0:用0来填充，8：填充8位，d:digital整数
# print(format(a,"08b"))
# print(format(a,"08x"))
# print(format(a,"08o"))
# # b = 1.25
# print(format(b, ".8f")) # 小数点后面保留xxx位

# # sorted
# lst = [111,2,32,21.213]
# res = sorted(lst)
# res1 = sorted(lst, reverse=True)
# print(res)
# print(res1)
#
# s = ["啊","大哥","别杀我","我给你钱"]
# # def func(item):
# #     return len(item)
# # ret = sorted(s, key=func, reverse=True)
# ret = sorted(s, key=lambda item: len(item))
# print(ret)

# lst = [
#     {"name": "盖伦", "hobby": "蹲草丛", "age": "13"},
#     {"name": "剑神", "hobby": "蹲草丛", "age": "12"},
#     {"name": "乌迪尔", "hobby": "蹲草丛", "age": "19"}
# ]
#
# ret = sorted(lst, key=lambda dic : dic['age'])
# print(ret)

# # filter 筛选操作
# lst = [21, 31, 313, 123, 44, 54, 55]
# f = filter(lambda x : x % 3 == 0,lst)
# # 把有用得东西提出出来
# print(f)
# print("__iter__" in dir(f)) # 可迭代的对象
# print(list(f))
#
# lst1 = [
#     {"name": "盖伦", "hobby": "蹲草丛", "age": "13"},
#     {"name": "剑神", "hobby": "蹲草丛", "age": "12"},
#     {"name": "乌迪尔", "hobby": "蹲草丛", "age": "19"}
# ] 
# f2 = filter(lambda item : int(item["age"]) > 12,lst1)
# # 把年龄大于12岁的筛选出来
# print(list(f2))

# map函数 做映射
lst = [1,22,33,44,55]
m = map(lambda x : x + 1,lst)
print(list(m))