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

# help
print(help(print)) # 对函数进行解释
# dir
s = "呵呵"
print(dir(s)) # 告诉你当前可以对其进行什么操作