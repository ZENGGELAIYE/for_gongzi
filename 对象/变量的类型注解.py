"""
变量设置类型主注解
基础语法： 变量 ： 类型
"""
import random
import json
# 基础数据类型注释
# var_1 : int = 10
# var_2 : float = 3.14
# var_3 : bool = True
# var_4 : str = "你好"

# 类对象型注释
class Student:
    pass
stu : Student = Student()

# 基础容器类型注解
my_list : list = [1,2,3]
my_tuple : tuple = (1,2,3)
my_set : set = {1,2,3}
my_dict : dict = {"年龄":12}
# 基础容器类型的详细注解
my_list : list[int] = [1,2,3]
my_tuple : tuple[int,str,bool] = (1,"你干嘛",True)
my_set : set[int] = {1,2,3}
my_dict : dict[str,int] = {"年龄":12}

def func(data):
    return 1
# 解释型注解
var_1 = random.randint(1,10) # type:int
var_2 = json.loads('{"你好"，”我不好“}') # type:dict
var_3 = func() # type:int

