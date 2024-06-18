import pizza # 导入pizza.py文件，可以执行其中包含的函数
pizza.make_pizza("大","萝卜","香菜")
pizza.abc()
pizza.dadada()

import pizza as pisa # 用as给pizza改个名，就可以直接用pisa了
pisa.make_pizza("大","萝卜","香菜")

from pizza import abc # 只想使用pizza中的abc模块就可以只导入abc模块
abc()

from pizza import abc as a # 只导入pizza文件中的abc模块给他重新命名为a就可以直接调用了
a()

from pizza import make_pizza, abc, dadada # 可以从其中调入多个模块，用逗号隔开
make_pizza(1,2)
abc()
dadada()

from pizza import *
# * 是导入pizza中的所有模块的意思，最好不用全部导入，以免程序名称重复出错。
# 在pizza文件中用__all__ = [] 定义了全部函数的内容
pizza.make_pizza(1,2)


