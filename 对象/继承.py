# 继承：单继承和多继承
class Phone:
    IMEI = None # 序列号
    produce = "HM"
    def call_ba_4g(self):
        print("4g通话")
class Phone2022(Phone): # 继承
    face_ID = 10010
    def call_ba_5g(self):
        print("5g通话")
class NFCReader:
    nfc_type = "第五代"
    producer = "HM"
    def read_card(self):
        print("NFC读卡")
    def write_card(self):
        print("NFC写卡")
class RemoteControl:
    rc_type = "红外遥控"
    def control(self):
        print("红外遥控开启了")
class Myphone(Phone2022,NFCReader,RemoteControl):
    pass
phone = Myphone()
print(phone.produce)
print(phone.face_ID)
phone.call_ba_4g()
phone.call_ba_5g()
phone.read_card()
phone.control()

class Phone1:
    IMEI = None # 序列号
    produce = "HM"
    def call_ba_4g(self):
        print("4g通话")
class Phone2:
    IMEI = None # 序列号
    produce = "123"
    def call_ba_5g(self):
        print("5g通话")
class Phone(Phone1,Phone2):
    pass
phone = Phone
print(phone.produce)