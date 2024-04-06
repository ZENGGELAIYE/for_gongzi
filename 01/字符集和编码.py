
"""
    编码总结：
    1.ascii：8bit, 1byte
    2.gbk:   16bit, 2byte  windows默认的
    3.unicode:32bit, 4byte
    4.utf-8:        mac默认
        英文：8bit,1byte
        欧洲：16bit,2byte
        中文：24bit,3byte

    gbk和utf-8是不能直接转换的
    我军密码本 -> 文字 -> 敌军密码本
"""

# 2.bytes
#   程序员平时所见的数据最终单位都是byte

# s = "周杰伦"
# bs1 = s.encode("gbk") # 对字符进行编码操作
# bs2 = s.encode("utf-8")
# print(bs1)  # b'\xd6'是byte类型 ， 一个\xd6就是一个字节
# print(bs2)

# # 怎么把一个gbk的字节转换为utf-8的字节
# bs = b'\xd6\xdc\xbd\xdc\xc2\xd7'
# s = bs.decode("gbk")   # 进行解码操作，转换成字符串
# print(s)
# bs1 = s.encode("utf-8") # 再进行编码操作，转换成bytes
# print(bs1)
#
# # 1. str.encode("编码") 进行编码
# # 2. bytes.decode("编码") 进行解码


