import requests
url = 'https://fanyi.baidu.com/sug'
s = input("输入你需要翻译的英文：")
dat = {
    "kw" : s
}
# 发送post请求，发生的数据必须放在字典中，通过data参数进行传递
resp = requests.post(url,data=dat)
print(resp.json()) # 将服务器返回的内容处理成json