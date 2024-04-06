"""
装饰器： -> 要求记住最后的结论
        装饰器本身上是一个闭包
        作用：
        在不改变原有函数调用的情况下，给函数增加新的功能
        直白：可以在函数前后添加新功能，但是不改变原来的代码

        在用户登陆的地方，日志。
        雏形：
        def wrapper(fn): # wrapper装饰器， fn目标函数
            def inner(*grgs,**kwargs):
            # 在目标函数之前执行的操作.......
            ret = fn(*args,**kwargs) # 执行目标函数,这样写函数也会被立即执行
            # 在目标函数之后执行的操作.......
            return ret
        return inner # 这里一定不能加括号
        @wrapper
        def target():
            pass
        target() # -> inner()
"""

# 智能的帮我开启外挂和关闭外挂
# def guanjia(name):
#     def inner():
#         print("外挂！启动")
#         name()
#         print("外挂，关闭！")
#     return inner
# @guanjia # 相当于play_dnf = guanjia(play_dnf)
# def play_dnf():
#     print("你好呀，我叫赛利亚，今天又是美好的一天")
# @guanjia # 相当于play_lol = guanjia(play_lol)
# def play_lol():
#     print("我的大刀已经饥渴难耐了")
#
# # play_dnf = guanjia(play_dnf) # 直接把管家的操作赋值给函数玩游戏,让管家把游戏重新封装一下
# # play_lol = guanjia(play_lol) # 一样的
#
# play_lol()
# play_dnf()

# def waigua(name):
#     def inner(*peo,**ple):
#         print("外挂，启动！")
#         name(*peo,**ple)
#         print("外挂，关闭！")
#     return inner
#
# @waigua # 表示play_dnf = waigua(play_dnf)
# def play_dnf(username,password):
#     print("你好呀，我叫赛利亚，今天又是美好的一天"+username+password)
# @waigua
# def play_lol(username,password,hero):
#     print("哈撒给！！！！！"+username+password+hero)
#
# play_dnf("i","123")
# play_lol("1","1","1")

# def waigua(name):
#     def inner(*args,**kwargs):
#         print("外挂启动")
#         ret = name(*args,**kwargs) # 这样弄的话函数也会被立即执行
#         print("外挂关闭！")
#         return ret
#     return inner
# @waigua
# def play_dnf(username,password):
#     print("你好啊，我叫赛利亚。",username,password)
#     print("今天又是美好的一天。")
#     return "流光星陨刀"
# @waigua
# def play_lol(username,password,hero):
#     print("我的大刀早已饥渴难耐奶了",username,password,hero)
#     print("去你妈的英雄联盟")
#     return "直接卸载"
# ret = play_dnf("1","2")
# res = play_lol("1","2","3")
# print(res)
# print(ret)
#
# def wrapper1(name):
#     def inner():
#         print("这是wrapper1，进入")
#         ret = name()
#         print("这是wrapper1，出")
#         return ret
#     return inner
#
# def wrapper2(name):
#     def inner():
#         print("这是wrapper2，进入")
#         ret = name()
#         print("这是wrapper2，出")
#         return ret
#     return inner
#
# @wrapper1
# @wrapper2
# def func():
#     print("你好呀，墨菲特")
# func()


# 装饰器运用
fc = True
def login_verify(fn):
    def inner(*args,**kwargs):
        global fc
        while fc:
            while 1:
                username = input("请输入用户名:")
                password = input("请输入密码:")
                if username == "admin" and int(password) == 123:
                    print("登陆成功")
                    fc = False
                    break
                else:
                    print("请输入正确的用户名或者密码")
        ret = fn(*args, **kwargs)
        return ret
    return inner
@login_verify
def add():
    print("添加用户信息")
@login_verify
def delet():
    print("删除用户信息")
@login_verify
def search():
    print("查找用户信息")

add()
delet()
search()