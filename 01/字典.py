# # 首先，字典是以键值对的形式来存储数据的。
# # 字典的表示方式 {key1:value, key2,value2, key3:value3}
# dic = {"诺手":"诺克萨斯之手", "盖伦":"德玛西亚"}
# # 字典的键必须是可哈希的
# val = dic["盖伦"] # 和列表差不多，只不过把索引换成了键索引
# print(val)

# 字典的键必须是可哈西的数据类型
# 字典的value数据类可以是任意的数据类型
# dic = {[]:123}
# # print(dic)
# dic = {"周杰伦":["dage",123]}

# 字典的新增
# dic = dict()
# dic["jay"] = "周杰伦"
# dic["1+1"] = 2
# print(dic)
# dic["jay"] = "昆凌" # 这里的字典新增操作只能是为替换操作，替换掉键jay的值
# print(dic)
# dic.setdefault("你好","hello")
# print(dic)
# dic.setdefault("jay","大哥") # 设置默认值，若果之前有了键jay，setdefault就不起作用了
# print(dic)

# 字典的删除
# dic = {'jay': '昆凌', '1+1': 2, '你好': 'hello'}
# dic.pop("jay") # 直接使用pop对键进行删除就行了
# print(dic)
# del dic["你好"] # del删除操作，比较麻烦，一般不适用
# print(dic)

# 字典的查询
# dic = {'jay': '昆凌', '1+1': 2, '你好': 'hello'}
# # print(dic["jay"])
# # print(dic.get("jay"))
#
# print(dic['jay001']) # 如果key不存在程序会报错。如果确定key的值的话就可以用这个方法。
# print(dic.get("jay001")) # 如果key不存在的话，程序返回None.不确定key的值的时候可以用
#
# dic = {
#     "天使":"后期无敌",
#     "诺手":"对线很猛",
#     "剑神":"屁用没得",
#     "乌迪尔":"团战搅屎棍"
# }
# name = input("请输入你想选择英雄姓名：")
# val = dic.get(name)
# if val == None: #也可以写 if val is None:S
#     print("你输出的英雄不在列表中")
# else:
#     print(f"你选择的英雄{val}")

# #字典的循环
# # 1.可以使用for循环，直接拿到key
# dic = {
#     "天使":"后期无敌",
#     "诺手":"对线很猛",
#     "剑神":"屁用没得",
#     "乌迪尔":"团战搅屎棍"
# }
# for key in dic:  # 这种方法遍历的是字典的键
# #     print(key, dic[key]) # 必须牢牢地记住
#
#
# #  希望直接拿到字典的的key和value
# dic = {
#     "天使":"后期无敌",
#     "诺手":"对线很猛",
#     "剑神":"屁用没得",
#     "乌迪尔":"团战搅屎棍"
# }
# print(dic.keys())  # 得到字典所有的key
# print(list(dic.keys()))  # 将所有字典的键存储在一个列表中
# print(dic.values())  # 得到字典所有的value
# print(list(dic.values()))  # 将字典所有的值存储在一个列表中

dic = {
    "天使":"后期无敌",
    "诺手":"对线很猛",
    "剑神":"屁用没得",
    "乌迪尔":"团战搅屎棍"
}
# 直接拿到字典中的key和value
for item in dic.items():
    print(item)
for key, value in dic.items():
    print(key,value)
#
# # a ,b = 1, 2 这个操作被称为解包，在元组和列表中均可以使用

# 字典的嵌套
# wangfeng = {"name":"wangfeng",
#             "wife":{
#                 "name":"zhangziyi",
#                 "age":"36",
#                 "hobby":"演戏",
#                 "assistant":{
#                     "name":"樵夫",
#                     "age":18
#                 },
#             "age":24,
#             "chiden":[
#                 {"name":"kid1","age":13},
#                 {"name":"kid2","age":13},
#                 {"name":"kid3","age":13}    ]}}
# print(wangfeng["wife"]["assistant"]["age"])
# wangfeng["wife"]["chiden"][0]["age"] = wangfeng["wife"]["chiden"][0]["age"] + 1
# print(wangfeng["wife"]["chiden"][0]["age"])

# 删除字典中姓乌的人
# dic = {
#     "天使":"后期无敌",
#     "乌手":"对线很猛",
#     "剑神":"屁用没得",
#     "乌迪尔":"团战搅屎棍"
# }
# # 也是用的和列表删除一样的手法，新建一个列表来存储需要删除的数据
# lis = []
# for item in dic:
#     if item.startswith("乌"): # 也可以写成 if item[0] == “乌”：
#         lis.append(item)
# for i in lis:
#     dic.pop(i)
# print(dic)
