class Phone:
    IMEI = None # 序列号
    produce = "HM"
    def call_ba_5g(self):
        print("5g通话")
# 定义子类，复写父类成员
class MyPhone(Phone):
    produce = "HM的新产品"
    def call_ba_5g(self):
        # 方法一
        print(f"父类的厂商是：{Phone.produce}") # 这个写道外面和里面都可以
        Phone.call_ba_5g(self) # 必须得写到函数里面
        # 方法二
        print(f"父类的厂商是：{super().produce}")
        super().call_ba_5g()
        print("5g通话来咯")
phone = MyPhone()
print(phone.produce)
phone.call_ba_5g()