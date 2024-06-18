# 对形参进行类型注解
def func(x:int,y:int): # 对形参进行类型注解直接在形参后面加冒号加他的类型就行了
    return x + y
# 对返回值进行类型注解
def func1(data:list) -> list:
    # 在函数名后面的那个位置加上一个-> 数据类型，就行了
    return data

from typing import Union
lst: list[Union[int,str]] = [1,3,"a"]
dic: dict[str,Union[int,str]] = {"a":1,"b":"c"}

def func(data:Union[str,int]) -> Union[str,int]:
    pass
