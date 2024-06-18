# 1.从服务器获取到网页源代码(urllib, request)
from urllib.request import Request, urlopen
import ssl
import re
# 干掉数字签名证书
ssl._create_default_https_context = ssl._create_unverified_context
def get_page(url):
    # 1. 准备请求信息
    r = Request(
        url,headers={
            # 用user-agent来模拟浏览器
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
        } # 在edge浏览器中找这个user-agent的时候要点一下原始
    )
    res = urlopen(r) # 发送请求
    return res.read().decode("utf-8") # 网页读取出来是二进制，要解码一下
get_page("https://movie.douban.com/top250")
# 2. 从网页源代码中提取到我想要的数据(re)
# 先准备好re
def parse_page(s):
    obj = re.compile('<div class="item">.*?<em class="">(?P<rank>.*?)</em>.*?'
                     '<span class="title">(?P<movie_name>.*?)</span>.*?'
                     '<span class="rating_num" property="v:average">(?P<grade>.*?)</span>.*?'
                     '<span>(?P<people_name>.*?)</span>',re.S)
    res = obj.finditer(s)
    lst = []
    for it in res:
        lst.append(it.groupdict())
    return lst
def main():
    f = open("电影.txt",mode="a",encoding="gbk")
    for i in range(10):
        s = get_page(f"https://movie.douban.com/top250?start={i*25}&filter=")
        data = parse_page(s)
        for it in data:
            f.write(str(it))
            f.write("\n")
main()