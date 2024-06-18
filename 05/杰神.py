"""
json有什么用
为了让不同的语言可以相互传递数据，Jason是一种很好的中转数据格式
"""
# json格式的数据要求很严格，下面我们来看一下他的要求
# json数据格式可以是：
{"name" : "admin", "age": 12}
# 也可以是：
[{"name" : "admin", "age": 12}, {"abc" : "asd", "size": 15}]
# 在python中json数据格式要么是字典，要么是列表，且列表中嵌套的必须是字典

# 导入json模块
import json

# # 准备一个列表，列表中的每一个元素都是字典，将其转换为json
# data = [{"name" : "大飞", "age": 12}, {"abc" : "小飞", "size": 15}]
# data = json.dumps(data, ensure_ascii= False)
# # 如果转换的内容中包括中文的话，加上ensure_ascii=False可以让中文正确显示
# print(data)
# print(type(data))
#
# # 准备一个字典，将其转化为json
# dic = {"name" : "周杰伦", "age": 12}
# dic_json = json.dumps(dic,ensure_ascii=False)
# print(dic_json)
# print(type(dic_json))

# # 将json转化为python字典数据类型
# s = '{"name" : "周杰伦", "age": 12}'
# l = json.loads(s)
# print(l,type(l))
#
# # 将json转化为python列表数据类型
# a = '[{"name" : "大飞", "age": 12}, {"abc" : "小飞", "size": 15}]'
# b = json.loads(a)
# print(b, type(b))

from pyecharts import options as opts
from pyecharts.charts import BMap
from pyecharts.faker import Faker

c = (
    BMap()
    .add_schema(baidu_ak="FAKE_AK", center=[120.13066322374, 30.240018034923])
    .add(
        "bmap",
        [list(z) for z in zip(Faker.provinces, Faker.values())],
        label_opts=opts.LabelOpts(formatter="{b}"),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="BMap-基本示例"))
    .render("bmap_base.html")
)
