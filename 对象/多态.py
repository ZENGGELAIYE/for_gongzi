# class Animal: # 父类只是用来确定有哪些方法，具体的调用还是通过子类来实现的
#     def speak(self):
#         pass # 这种空实现的方法被称为抽象类(也可以被叫做接口)
# class Dog(Animal):
#     def speak(self):
#         print("汪汪汪")
# class Cat(Animal):
#     def speak(self):
#         print("喵喵喵")
# def make_noise(animal:Animal):
#     animal.speak()
# dog = Dog()
# cat = Cat()
# make_noise(dog)
# make_noise(cat)

# 抽象类好比一个标准，要求子类必须得实现
class AC: # 定义一个抽象类，把需要执行的内容丢进去
    def cold_wind(self):
        pass
    def hot_wind(self):
        pass
    def swing_l_r(self):
        pass
class Midea(AC):
    def cold_wind(self):
        print("美的空调制冷")
    def hot_wind(self):
        print("美的空调炽热")
    def swing_l_r(self):
        print("美的空调摆风")
class Greed(AC):
    def cold_wind(self):
        print("格力空调制冷")
    def hot_wind(self):
        print("格力空调炽热")
    def swing_l_r(self):
        print("格力空调摆风")
def make_cold(ac:AC):
    ac.cold_wind()
midea = Midea()
greed = Greed()
make_cold(midea)
make_cold(greed)