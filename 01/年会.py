# # 年会抽奖小程序 300个员工，30个三等奖，6个二等奖，3个一等奖，不能重复中奖
# lst = list()  #建立一个空表格
# for i in range(1,301): # 建立一个300个员工的列表
#     a = f"员工{i}"
#     lst.append(a)
# # print(lst)
# third_prize = []
# second_prize = []
# big_prize = []
# import  random # 导入随机模块
# third_prize = random.sample(lst,30) # 从列表从挑30个人出来是三等奖
# for i in third_prize:
#     lst.remove(i)    # 把列表中的这30个人删除掉，免得重复中奖
#     print(f"{i}中了三等奖,避孕套一盒")
# second_prize = random.sample(lst, 6)
# for i in second_prize:
#     lst.remove(i)
#     print(f"{i}中了二等奖,iPhone手机一个")
# big_prize = random.sample(lst, 3)
# for i in big_prize:
#     print(f"{i}中了一等奖泰国五日游")


import random # 导入随机模块,要进行随机操作必有这步
print(random.randint(12,18))  # 从中随机抽取一个整数，可以取到两边的数
lst = [11,22,33,44,55,66]
print(random.choice(lst))      # 从列表中随机抽取一个样本
print(random.sample(lst,4))   # 从列表中随机抽取4个样本
