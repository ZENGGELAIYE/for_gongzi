"""
    返回值：函数执行之后，会给调用方一个结果，这个结果就是返回值

    关于return:
    函数执行到了return，函数就会立即停止并返回内容，函数内的return的后续代码不会执行
    1.如果函数没有return，此时外界收到的是None
    2.如果只写了return
        1.只写了return，后面不跟数据，此时接受到的任是None ——> 相当于break
        2.return值，此时的表示函数只有一个返回值，外界能够收到一个数据 ——> 用的最多
        3.return 值1， 值2， 值3.....,此时函数有多个返回值，外界收到的是元组，并且，该元组存储所有的返回值
"""

# def func():
#     print(123)
#     return  # 程序执行到return的时候就会直接结束， 后面的代码不会执行，就像break
#     print(456)
# ret = func()
# print(ret)
#
# def func(a, b):
#     return a + b
# ret = func(3, 4)
# print(ret)

def func():
    return 1,2,3,4
ret = func()
print(ret)