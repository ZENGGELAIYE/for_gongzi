# lst = []
# for i in range(1, 11):
#     lst.append(i)
# print(lst)

# # 列表推导式的基本语法：[结果 for循环 if条件]
# lst = [i for i in range(1, 11)]
# print(lst)
# # 把一到十的偶数添加进去
# lst1 = [i for i in range(1, 11) if i % 2 == 0]
# print(lst1)
# # 把一到十的偶数的平方添加进去
# lst2 = [i ** 2 for i in range(1, 11) if i % 2 == 0]
# print(lst2)
#
# # python x 1 ~ python x ~ 250
# lst = [f"python x %i" % i for i in range(1, 251)] # %s 表示
# print(lst)

# # 字典推导式： {key:value for循环 if条件判断}
# lst = ["你好", "你好呀", "你太好了"]
# dic = {i:lst[i] for i in range(len(lst))}
# print(dic)

# # 集合推导式
# lst = ["张无忌", "张无忌", "张三丰"]
# s = {item for item in lst}
# print(s) # 集合可以去重

l = (i + 1 for i in range(10))
print(l)