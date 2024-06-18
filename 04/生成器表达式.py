# g = (i for i in range(10))
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# 拿空生成器中的数据
# 1. 直接使用for 循环
# 生成器 -> 迭代器 -> 可迭代对象 -> for循环
# for i in g:
#     print(i)

# 2. 可以使用 list, tuple, set 直接拿空
# print(set(g))
# print(tuple(g))
# print(list(g))

# def func(): # 生成器函数
#     print(123)
#     yield 222
# g = func() # 创建生成器
# g1 = (i for i in g) # g1也是生成器
# g2 = (i for i in g1) # g2也是生成器
#
# print(list(g)) # 这里直接把g拿空了，后面的g1和g2就没有数据了
# print(list(g1))
# print(list(g2))

def func():
    lst1 = ["沈腾1", "玛丽1", "麻花1"]
    lst2 = ["沈腾2", "玛丽2", "麻花2"]
    # for i in lst1:
    #     yield i
    # for i in lst2:
    #     yield i
    yield from lst1 # 把一个可迭代对象的每一项返回
    yield from lst2
g = func()
print(list(g))