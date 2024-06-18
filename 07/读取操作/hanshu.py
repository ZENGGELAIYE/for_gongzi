import json
f = open('练习.txt',mode="r",encoding="utf-8")
date = f.readlines()
for item in date:
    item = item.strip()
    item = item.replace("'",'"')
    item = json.loads(item)
    print(item,type(item))