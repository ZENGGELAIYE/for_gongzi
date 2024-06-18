class Phone:
    __is_5G_enable = False
    def __check_5G(self):
        if self.__is_5G_enable == True:
            print("5G开启")
            return True
        else:
            print("5G关闭")
            return False
    def call_by_5G(self):
        if self.__check_5G() == True:
            print("正在5G通话中")
        else:
            print("正在4G通话中")
phone = Phone()
phone.call_by_5G()