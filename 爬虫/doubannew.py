import requests
url = 'https://movie.douban.com/j/chart/top_list'
# 重新封装参数
para = {
    'type': '24',
    'interval_id': '100:90',
    'action': '',
    'start': 0,
    'limit': 100,
} # 这儿的params相当于再url后面加上？之后的内容
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
} # 处理了一个反爬
resp = requests.get(url=url, params=para,headers=headers)
print(resp.json())
resp.close() # 关掉resp