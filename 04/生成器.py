"""
生成器函数：
    1.里面有yield
    2.生成器函数再执行的时候实际是创造一个生成器出来。
    3.必须使用__next__()来执行一个代码，会自动的执行到下个yield结束
    4.yield也是返回值得意思，可以让一个函数分段执行
    5.当后面没有yield之后，再次__next__()会报错StopIteration
"""
# def func(): # 生成器函数
#     print(123)
#     print(222)
#     yield "你好" # 当函数中有yield的时候函数就是生成器函数，yield也有返回的意思
#     print(456)
#     print(444)
#     yield "我叼你妈"
# gen = func() # 生成器函数在被执行的时候产生生成器。
# print(gen) # <generator object func at 0x000002550B195000>
# ret1 = gen.__next__() #可以让生成器执行到下一个yield
# print(ret1)
# ret2 = gen.__next__()
# print(ret2)
# ret3 = gen.__next__() # 当程序后面没有yield的时候程序会报错。StopIteration
# print(ret3)

# 节省内存
# 买10000件衣服
# def order():
#     lst = []
#     for i in range(10000):  # 会比较消耗资源
#         lst.append(f"衣服{i}号")
#     return lst # 列表占内存
#
# lst = order()
# print(lst)

# 买10000键衣服，生成器版本
# def order():
#     for i in range(10000):
#         yield f"衣服{i}号" # 这样的话相当于只是在内存中存储了一个order函数，要用的时候就调用一下更加节省空间。
# genator = order()
# print(genator.__next__())
# print(genator.__next__())
# print(genator.__next__())
# print(genator.__next__())
# print(genator.__next__())

# 每次拿50件衣服版本
# def order():
#     lst = []
#     for i in range(10000):
#         lst.append(f"衣服{i}号")
#         if len(lst) == 50:
#             yield lst # 当执行到yield时返回个长度为50的列表，继续向下执行时列表会被清空
#             lst = []
#         else:
#             continue
#     return lst
# g = order()
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# send()
"""
__next__()
send()
    相同点：可以执行到下一个yield
    不同点：send可以给上一个yield位置传值
"""
def func():
    print("111")
    a = yield "西红柿"
    print("你好", a)
    b = yield "南瓜"
    print("你来了", b)
    yield "搞快点"

g = func()
print(g.__next__()) # 要用send的话第一个必须得用__next__()，因为如果用了send的话没办法给上一个yield传值
print(g.send("哈哈")) # 给上一个yield传值”哈哈“
print(g.send("呵呵"))