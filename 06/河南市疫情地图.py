import json
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts,TitleOpts
f = open("D:\BaiduNetdiskDownload\资料\第1-12章资料\资料\资料\可视化案例数据\地图数据\疫情.txt",
         mode="r", encoding="utf-8")
data = f.read()
f.close()
data_dict = json.loads(data)
cities_date = data_dict["areaTree"][0]["children"][3]["children"]
cities_list = []
for city_data in cities_date:
    city_name = city_data["name"]+'市'
    city_confirm = city_data["total"]["confirm"]
    cities_list.append((city_name, city_confirm))
print(cities_list)
map = Map()
map.add("河南地图",cities_list,"河南")
map.set_global_opts(
    title_opts=TitleOpts("河南市确诊人数",pos_bottom="1%",pos_left="center"),
    visualmap_opts=VisualMapOpts(
        is_show=True, # 是否显示
        is_piecewise=True, # 是否分段显示
        pieces=[
            {"min": 1, "max": 99, "label": "1-99", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "100-999", "color": "#FF6666"},
            {"min": 1000, "max": 2000, "label": "1000-2000", "color": "#990033"},
            {"min": 2001, "max": 5000, "label": "2001-5000", "color": "#990033"},
            {"min": 5001, "label": "5000以上", "color": "#990033"}
        ]
    )
)
map.render("河南省却总人数.html")