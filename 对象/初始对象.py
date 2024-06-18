# 设计一个类
class Student:
    name = None
    gender = None
    nationality = None
    native_place = None
    age = None
# 创建一个对象
stu_1 = Student()
# 对象属性进行赋值
stu_1.name = "盖伦"
stu_1.gender = "男"
stu_1.nationality = "德玛西亚"
stu_1.native_place = "德玛西亚的城堡里"
stu_1.age = 31
# 捕获对象中记录的信息
print(stu_1.name)
print(stu_1.gender)
print(stu_1.nationality)
print(stu_1.native_place)
print(stu_1.age)
