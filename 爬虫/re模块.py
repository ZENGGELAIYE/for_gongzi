import re
s = ('<div class="gql"><span id ="1">郭麒麟</span></div>'
     '<div class="zjl"><span id ="2">周杰伦</span></div>'
     '<div class="gbt"><span id ="3">郭碧婷</span></div>'
     '<div class="ljj"><span id ="4">林俊杰</span></div>'
     '<div class="sdd"><span id ="5">萨顶顶</span></div>')
# (?P<分组名称>正则) 可以从正则内容中进一步提取内容
res = re.compile(r'<div class="(?P<abbreviation>.*?)">'
                 r'<span id ="(?P<id>.*?)">(?P<name>.*?)</span></div>',re.S)
# re.S 表示.可以匹配包括换行符在内的所有字符
result = res.finditer(s)
for it in result:
    print(it.group("abbreviation"))
    print(it.group('id'))
    print(it.group())
    print(it.groupdict())