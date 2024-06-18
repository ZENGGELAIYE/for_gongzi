from urllib.request import urlopen
baidu = 'http://www.baidu.com/'
res = urlopen(baidu)
# print(res.read().decode('utf-8'))
with open("baidu.html",mode='w',encoding='utf-8') as f:
    f.write(res.read().decode('utf-8')) # 读取到了网页的源代码
print('over')