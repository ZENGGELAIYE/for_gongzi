"""
参数：可以在函数调用的时候，给函数传递一些信息
分类：
    1.形参,在函数定义的时候，需要准备一些变量来接受信息
        1.位置参数，按照位置位置一个一个的去声明变量
        2.在函数声明的时候给变量一个默认值，如果实参不传递信息，此时默认值生效，否则不生效。
        3.动态传参
            1.*(args)，表示接受所有位置的动态传参
            2.**(kwargs), 表示接受所有的关键字的动态传参
    顺序： 位置 > *args > 默认值 > **kwargs
    2.实参，实际调用的时候转递信息
        1.位置参数。按照位置进行传递参数
        2.关键字参数。按照参数的名字进行传递参数
        3.混合参数
            顺序：位置参数放前面，关键字参数放后面   ->  否则会报错
        实参在执行的时候必须，保证保证形参有数据。
"""

# 骂人。骂谁？骂道什么程度？
# def rude_somebody(ren,lvl):
#     print("怒目而视"+ren)
#     print("开始输出"+ren)
#     if lvl > 100:
#         print("老子打屎你"+ren)
#     else:
#         print("你是臭傻逼"+ren)
#     print("滚吧你"+ren)
#
# rude_somebody(input("请输入你想骂的人的名字："),int(input("你对他的不满等级（用数字表示）：")))

# # 做一个四则运算
# def yunsuan(a,op,b):
#     if op == "+":
#         print(a + b)
#     elif op == "-":
#         print(a - b)
#     elif op == "*":
#         print(a * b)
#     elif op == "/":
#         print(a / b)
#     else:
#         print("去你妈的")
# yunsuan(1111,"+",1)
# yunsuan(1111,"-",1)
# yunsuan(1111,"*",1)
# yunsuan(1111,"/",1)

# def chi(zhu,fu,tang,tianping):
#     print(zhu,fu,tang,tianping)
# chi("米饭","土豆丝","鸡蛋汤","蛋糕") #位置参数
# chi(zhu="米饭",fu="土豆丝",tang="鸡蛋汤",tianping="蛋糕") #关键字参数
# chi("米饭","土豆丝",tang="鸡蛋汤",tianping="蛋糕") #混合参数

# 默认值参数
# 在函数声明的时候给变量一个默认值，如果实参不传递信息，此时默认值生效，否则不生效。
# def luru(name,age,gender="男"):
#     print(name,age,gender)
# luru("张三",13)
# luru("小丽",17,"女")
# luru("大飞",12)
# luru("李四",14)

# # 位置动态传参
# def chi(*food): # * 表示位置传参的动态传参，*接受的值会被同意放在一个元组里面。
#     print(food)
# chi("米饭","蛋花汤","皮蛋" ,"鸡蛋糕")
# chi("米饭","蛋花汤","皮蛋" )
# chi("米饭","蛋花汤")
# chi("米饭",)

# # 关键字动态传参
# def chi(**food):  # **表示接受关键字的动态传参，接收到的所有参数都会被处理成字典。
#     print(food)
# chi(fan="大米饭",cai="番茄炒蛋" )

# def func(a, *args, b = "哈哈", **kwargs): # 位置 > *args > 默认值 > **kwargs
#     print(a, args, b, kwargs)
#
# func(1, 2, 3, b = "呵呵", sb = "杰哥", 帅哥 = "曾磊")

# 补充
# lst = ["大佬","牛逼","卧槽","别鸡巴卧槽了"]
# dic = {"a":"你啊", "b":"来啊", "c":1}
# def func(*liebiao):
#     print(liebiao)
# def funca(**zidian):
#     print(zidian)
# func(*lst) # * 在实参位置，是把列表打散成位置参数进行传递
# funca(**dic) # ** 在实参位置，可以把字典自动转化为关键字参数进行传递