import re
# 1.从一个字符串中提取到所有的数字
# lst = re.findall("\d+","我今年18岁了，我一次性吃8碗饭")
# print(lst)

# # 2.判断一句话中是否有数字
# # search的特点:匹配字符串，匹配到第一个结果就返回，不会匹配出多个结果来
# res = re.search("\d+","我今年18岁了，我一次性吃8碗饭")
# print(res.group())
# print(res.group()) # 不加group的话得到的是一个match对象

# # 3. finditer所有数据都会进行匹配，返回的是迭代器
# res = re.finditer("\d+","我今年18岁了，我一次性吃8碗饭")
# print(res.__next__().group())
# print(res.__next__().group())

# 4. match 匹配，从头开始匹配
# result = re.match("\d+","18岁了，我一次性吃8碗饭")
# print(result.group())

# 5.split 切割
# result = re.split("\d+","你好呀1，我是2赛利亚")
# print(result)
# res = re.split("[你好]","你在干嘛呀，我好无聊啊，有一点想你")
# print(res) # 放在[]中的字符串每个都会参加切割
# res1 = re.split("你好","你在干嘛呀，我好无聊啊，有一点想你好")
# print(res1) # 而没有用[]括起来的字符串必须得一起用才能生效

# 6. sub替换操作
# result = re.sub("\d+","sb","你是1吗？臭2")
# print(result)
# # 替换多少次
# result1 = re.subn("\d+","sb","你是1吗？臭2")
# print(result1)

# 7. compile操作
# result = re.compile("\d+") # 先加载这个正则，后面可以直接用这个去匹配内容
# print(result.findall("我今天吃了3个方便面，喝了2瓶子汽水"))

# 8. 爬虫必会的一个重点
# 1.()括起来的内容是你最终想要的结果
# 2.(?P<name>正则)把正则匹配到的内容直接放在name组里面，后面取数据的时候直接group(name)
obj = re.compile(r"今天吃了(?P<mian>\d+)个面，(?P<zhou>\d+)碗粥")
# 正则表达式经常出现\n,为了避免这种问题出现，可以在字符串前面加上r来直接把字符串中的内容当作普通字符串来处理
result = obj.finditer("我昨天吃了3个鸡蛋，今天吃了3个面，1碗粥，明天想吃4个面包")
for it in result:
    print(it.group("mian"))
    print(it.group("zhou"))
    print(it.groupdict())