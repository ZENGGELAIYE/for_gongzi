"""
闭包： 本质，内层函数对外层函数的局部变量的使用。此时内存函数被称为闭包函数
    1.可以让一个变量常驻与内存
    2.可以避免全局变量被修改
"""
def func():
    a = 10
    def inner():
        nonlocal a
        a += 1
        return a
    return inner # 返回函数inner不能加括号，加上括号就是执行代码的意思，就不再是返回代码的意思
ret = func()
s1 = ret()
print(s1)
s2 = ret()
print(s2)
# 如果给return的inner加上括号
# ret = func()
# s1 = ret
# print(s1) # 执行一次inner，程序结束，a从10变成11
# s2 = ret
# print(s2) # 执行一次inner，程序结束，a从10变成11