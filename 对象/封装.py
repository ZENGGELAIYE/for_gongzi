"""
定义私有成员和方法的方式
    私有成员变量：变量以__开头(两个下划线)
    私有方法变量：方法以__开头(两个下划线)
"""
# class Phone:
#     __current_voltage = None # 定义私有变量电压
#     def __keep_single_core(self):
#         print("让CPU以单核运行")
# phone = Phone()
# phone.__keep_single_core() # 私有方法不可以直接调用
# print(phone.__current_voltage) # 私有变量也不可以直接调用

class Phone:
    __current_voltage = 1 # 定义私有变量电压
    def __keep_single_core(self):
        print("让CPU以单核运行")
    def call_by_5G(self):
        if self.__current_voltage >= 1:
            print("现在是5G通话哦")
        else:
            self.__keep_single_core()
            print("现在CPU单核运转不是5G通话")

phone = Phone()
phone.call_by_5G()