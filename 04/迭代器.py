# for c in "你好":
#     print(c)
#
# for a in 123: # int类型不可以被迭代(iterable)
#     print(a)
# dir 函数可以执行的功能
# print(dir(str))  # 有__iter__
# print(dir(list)) # 也有__iter__
# print(dir(dict)) # 也有__iter__
# print(dir(int))  # 没有__iter__
# print("__iter__" in dir(bool)) # bool也没有__iter__
#
# # iterable 可迭代的
# # 所有可迭代的对象内部都含有一个__iter__的功能
# lst = ["你好","你很好","你不好"]
# it = lst.__iter__() # iterator 迭代器
# print(it)
# print(dir(it)) # __next__ 下一个
# ret =  it.__next__()
# print(ret) # 你好
# ret =  it.__next__()
# print(ret) # 你很好
# ret =  it.__next__()
# print(ret) # 你不好
# ret =  it.__next__()
# print(ret) # 程序报错，StopIteration
# 使用步骤
# 1. 通过__iter__()拿到迭代器
# 2. 用迭代器执行__next__()拿到元素
# 3. 重复第二步，直到程序报错 StopIteration

s = {"打啊打","大数据的","Dnsa"}
# it = s.__iter__()
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# # 1.迭代到头了想要重新拿数据，需要重新拿迭代器
# it = s.__iter__()
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

# 2.这里不适合使用数学上的等价代换
# s = {"打啊打","大数据的","Dnsa"}
# print(s.__iter__().__next__()) # 为什么每次打印的结果都一样呢
# print(s.__iter__().__next__()) # 因为每次都重新赋值了一个迭代器
# print(s.__iter__().__next__())

# s = {"打啊打","大数据的","Dnsa"}
# it = iter(s)   # iter = __iter__()
# print(next(it)) # next = __next__()
# print(next(it))
# print(next(it))

lst = []
it = lst.__iter__()
print(dir(lst)) # 列表不是一个迭代器
print(dir(it)) # 迭代器本身是一个可迭代对象，迭代器可以使用for循环