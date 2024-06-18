class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age #__init__只能return一个None
    def __str__(self): # 字符串方法
        return f"Student类，姓名{self.name},年龄：{self.age}"
    def __lt__(self, other): # 小于和大于两种比较
        return self.age > other.age
    def __le__(self, other): # 小于等于和大于等于两种比较
        return self.age > other.age
    def __eq__(self, other): # 是不是相等判断
        return self.age == other.age
stu1 = Student("周杰伦",13)
stu2 = Student("林俊杰",16)
print(stu1)
print(stu2)
print(stu1 < stu2)
print(stu1 <= stu2)
print(stu1 == stu2)