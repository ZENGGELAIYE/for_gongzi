"""
函数可以嵌套函数

综上
    1；函数可以作为返回值进行返回
    2；函数可以作为参数进行互相传递
    函数名实际上就是一个变量名，都表示一个内存地址
"""
# def func():
#     a = 20
#     def func1(): # 函数的嵌套，局部变量
#         print(123)
#     print(a)
#     return func1()   # 函数都会有一return，当在直接打印的时候都会把return的值给打印出来
# print(func())  # return没有值的时候会返回一个return

# def func1():
#     print(123)
#     def func2():
#         print(456)    # 123 4 456 1 789 3
#         def func3():
#             print(789)
#         print(1)
#         func3()
#         print(3)
#     print(4)
#     func2()
#     print(6)
# func1()

# def func():
#     def inner():
#         print(123)
#     print(inner) # inner不加括号打印出来是<function func.<locals>.inner at 0x0000015270E89A80>
#                  # function函数，点可以读成的，locals是局部的意思
#     return inner # 返回的是一个函数，此时我们把函数当成一个变量来进行返回
# b1 = func() # b1 是func内部的inner
# print(b1)
# b1()

# def an():
#     print(123)
# b1 = an # 函数名就想读于是一个变量
# print(b1) # 函数可以作为一个参数相互传递
# b1()

# global nonlocal
# a = 10
# def func():
#     global a # 把外面的全局变量引入到局部进行修改
#     a = 20 # 创建一个局部变量，并没有办法修改全局变量中的a
# func() # 调用函数使a变成20
# print(a)

def func1():
    a = 10
    def func2():
        nonlocal a #向外找一层，看看有没有该变量，如果有就引入，如果没有就继续往外找，直至全局（不包括全局）
        # 如果找不到的话就会报错
        a = 20
    func2()
    return a
print(func1())