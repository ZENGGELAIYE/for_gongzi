# # set集合，set集合是无序的
# s = {1, 2, "hehe", 3}
# # print(s)
#
# s = {1, 2, "haha",[]} # unhashable type :'list'
# print(s)
# 不可哈希：python中的set集合进行数据存储的时候，需要对数据进行哈希计算，根据计算出来的哈希值进行存储数据
#         set集合要求存储的数据必须是可以进行哈希计算的。
# 不可哈希：可变的数据类型：list, dict, set.
# 可哈希：不可变的数据类型，int， str, tuple(元组)， bool.

# # 创建空集合
# s = set()
# s.add("赵本山")
# s.add("范伟")
# s.add("狗日的")
# print(s)
# # s.pop()  #pop删除集合的最后一个元素
# # #由于集合无须，测试的时候无法验证最后一个是什么。
# # print(s)
# # s.remove("范伟")
# # print(s)
# s.remove("赵本山")
# s.add("马化腾")
# print(s)

# s = {'狗日的', '范伟', '马化腾'}
# for item in s:
#     print(item)

#交集 并集 差集
# s = {"刘能","赵本山","范伟"}
# a = {"赵本山","诺手","奥拉夫"}
# print(s & a) # 表示交集
# print(s.intersection(a)) # 表示交集
#
# print(s | a)
# print(s.union(a)) #表示并集
#
# print(s - a)
# print(s.difference(a))

# 重要的作用，可以去除重复
s = {"周杰伦","昆凌","蔡依林","田馥甄"}
print(s)
s.add("周杰伦") # set集合里面不会出现重复的数据
print(s)

lst = ["周杰伦","昆凌","蔡依林","田馥甄","周杰伦","昆凌","蔡依林","田馥甄",]
print(lst)
print(set(lst)) #类型变成了set集合
print(list(set(lst))) #把类型重新转换为列表，但是输出的列表是无序的