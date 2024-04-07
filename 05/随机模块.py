# import random
# print(random.random()) # 打印一个从0到1的随机小数，取不到0和1
# print(random.uniform(5,10)) # 打印一个从5到10的小数，娶不到两边
# print(random.randint(3,10)) # 打印一个3到10的随机数可以取到两边
#
# lst = ["诺手","蔡徐坤","娜美","火男"]
# print(random.choice(lst)) # 随机抽取一个
#
# lst2 = ["青龙刀","魔剑","流光星陨刀","光剑","太刀"]
# print(random.sample(lst2,3)) # 从什么东西中随机抽取3个元素

import random
# 搞一个验证码
def num():
    return str(random.randint(0,9)) # 把数字转化成字符
def upper():
    return chr(random.randint(65, 90)) # chr表示把数字换成字母
def lowwer():
    return chr(random.randint(95, 122))
lst = []
def random_verify_code(number = 4): # 默认为4位数的验证码
    global lst # 把外面的列表拿进来
    for i in range(int(number)):
        n = random.randint(0,2)
        if n == 0:
            a = num() # a就是函数返回的值
        elif n == 1:
            a = upper()
        elif n == 2:
            a = lowwer()
        lst.append(a)
    return "".join(lst) # 把列表中的元素用""中的东西隔开输出为字符串
print(random_verify_code(6)) # 输出一个六位数的代码，把默认值4替换了