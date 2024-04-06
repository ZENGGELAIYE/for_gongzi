# # # couple元组，特点：不可变
# t = ("sb","fw","haha")
# # print(t)
# # print(t[1])
# # print(t[1:3])
# t[0] = "dageda"
# print(t)

# 你固定了某些数据不希望外界修改
# 元组只有一个元素（*）,需要在元素得末尾加一个逗号
# t = ("哈哈")
# print(t)
# print(type(t))
# c = ("哈哈",)
# print(type(c))

# 元组的不可变（坑）
t = (1, 2, 2, ["haha","didi"])
t[3][1] = "asd"
print(t)