import re
import requests
import csv
def page_operation(url, headers):
    rep = requests.get(url, headers=headers)
    return rep.text
url = 'https://movie.douban.com/top250'
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
}
context = page_operation(url, headers)
def re_operation(context):
    result = re.compile(r'<span class="title">(?P<name>.*?)</span>.*?<br>(?P<year>.*?)&nbsp'
                        r'.*?<span class="rating_num" property="v:average">(?P<grade>.*?)</span>'
                        r'.*?<span>(?P<number>.*?)</span>',re.S)
    a = result.finditer(context)
    f = open('data.csv', mode='a',newline='')
    # newline = '' 文件里面有空白行的时候可以加一下，消除空白行
    csv_write = csv.writer(f)
    for it in a:
        dic = it.groupdict()
        dic['year'] = dic['year'].strip()
        csv_write.writerow(dic.values())
    f.close()
def main():
    for i in range(10):
        s = page_operation(f"https://movie.douban.com/top250?start={i*25}&filter=",headers)
        re_operation(s)
main()