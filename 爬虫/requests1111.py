import requests
url = "https://www.sogou.com/web?query=周杰伦"
dic = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0"
}
resp = requests.get(url, headers=dic) # 处理了一个反爬
# get方式一般都适用于网址的输入
print(resp)
print(resp.text) # 这样就可以拿到页面源代码