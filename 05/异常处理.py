# try:
#     print(1/0)
# except:
#     print("程序出错了，请联系程序员。")

"""
try:
    try代码
except 错误1 as 变量1：
    except1代码
except 错误2 as 变量2：
    except2代码
except Exception as e： 防止没有统计完全错误导致程序报错
    exception代码
......
finally:
    收尾
"""
#
# try:
#     # print(1/0)
#     open("dasdasda",mode='r',encoding='utf-8').read()
#     # lst = []
#     # lst.pop(1)
# except (ZeroDivisionError,NameError) as z: # 还可以多包涵几个异常处理
#     print("除数为0")
# except FileNotFoundError as f:
#     print("没有找到文件")
#     print(f)
# except Exception as e:
#     print("系统错误")
# finally: # 不论程序报不报错都要执行收尾
#     print("收尾")
#
# try:
#     print(name)
#     1/0
# except Exception: # 抓取全部异常
#     print("出现异常了")
# else: # 没有异常就执行else
#     print("很高兴，没有异常")
# finally: # 有没有异常都得执行finally
#     print("我是finally，有没有异常我都要执行")

# 异常是可以自己跑出去的
# def func(a, b):
#     if type(a) == int and type(b) == int:
#         print(a + b)
#     else:
#         # 抛出一个异常
#         raise Exception("你给我的数更笨没有办法进行加减")
#
# func(12, 12)
# #

# 异常具有传递性
def func1():
    print("func1开始执行")
    num = 1/0
    print("func1结束执行")

def func2():
    print("func2开始执行")
    func1()
    print("func2结束执行")

def main():
    try:
        func2()
    except Exception as e:
        print(f"函数运行出错，问题是{e}")

main()