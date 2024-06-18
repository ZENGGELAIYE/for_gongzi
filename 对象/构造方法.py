# class Student:
#     def __init__(self,name,age,gender):
#         # __init__被称为构造方法，在定义对象的时候就会自动执行。
#         self.name = name  # 这个操作的意思是，创建一个name变量，并且要调用它必须加上self来进行赋值
#         self.age = age
#         self.gender = gender
#         print("好了，赋值完成")
# stu = Student("周杰伦","41","男")
# print(stu.name,stu.gender,stu.age)

class Register_system:
    def __init__(self):
        for i in range(10):
            name = input("请输入姓名：")
            age = input("请输入年龄：")
            address = input("请输入地址：")
            print(f"姓名：{name},年龄：{age}，地址：{address}")
            # 方法内的变量不是成员变量，不需要用self来调用
register_system = Register_system()