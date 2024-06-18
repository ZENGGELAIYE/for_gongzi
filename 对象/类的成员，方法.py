"""
class 类名称：
    类的属性    ~类的属性，即是定义在类中的变量（成员变量）
    类的行为    ~类的行为，即是定义在类中的函数（成员方法）
"""
# 创建一个带有成员方法的类
class Student:
    name = None
    def say_hi(self): # self是必须存在的，可以不传参
        print(f"你好呀，我叫{self.name}，请多多关照") # 调用类的成员变量时必须加上self
    def say_msg(self,msg):
        print(msg)

stu1 = Student()
stu1.name = "周杰伦"
stu1.say_hi()
stu1.say_msg("哎哟不错哟")

stu2 = Student()
stu2.name = "林俊杰"
stu2.say_hi()
stu2.say_msg("小伙子，我看好你")

