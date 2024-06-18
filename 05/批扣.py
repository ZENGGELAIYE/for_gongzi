# import pickle
# lst = ["诺手","天使","蛤蟆","盖伦"]
# print(pickle.dumps(lst)) # 把这个东西转化成字节
#
# s = b'\x80\x04\x95)\x00\x00\x00\x00\x00\x00\x00]\x94(\x8c\x06\xe8\xaf\xba\xe6\x89\x8b\x94\x8c\x06\xe5\xa4\xa9\xe4\xbd\xbf\x94\x8c\x06\xe8\x9b\xa4\xe8\x9f\x86\x94\x8c\x06\xe7\x9b\x96\xe4\xbc\xa6\x94e.'
# a = pickle.loads(s) # 再把字节转化成它原来的东西
# print(a)

# import pickle
# lst = ["诺手","天使","蛤蟆","盖伦"]
# f = open("英雄联盟.txt",mode= "w",encoding="utf-8") # 使用w写入模式写入东西
# f.write(str(lst)) # 只能写入str和int类型
# f.close()
#
# r = open("英雄联盟.txt",mode="r",encoding="utf-8")
# n = r.read()
# print(n)
# print(type(n)) # 列表打印出来的类型是str改变了其数据类型

# import pickle
# dic = {"name":"admin","password":123}
# pickle.dump(dic,open("abc.txt",mode="wb")) # 把字典转化成字节存储在文件中（wb以字节形式写）
#
# s = pickle.load(open("abc.txt",mode="rb")) # 把文件中的字节读取出来
# print(type(s)) # 这样的话他的数据类型就不会发生改变

"""
序列化：把对象转化成二进制字节
反序列化：把二进制字节转回为对象
1.dumps   把对象(数据)转化为字节
2.loads   把字节转化会对象(数据)
3.dump    把对象序列化成字节之后写入到文件
4.load    把文件中的字节反序列化成对象
"""