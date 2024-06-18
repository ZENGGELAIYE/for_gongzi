import json
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts, TitleOpts
# 读取文件
f = open("D:\BaiduNetdiskDownload\资料\第1-12章资料\资料\资料\可视化案例数据\地图数据\疫情.txt",
         mode="r", encoding="utf-8")
data = f.read()
# 关闭文件
f.close()
# 取到各省的数据
data_dict = json.loads(data)
province_data_list = data_dict["areaTree"][0]["children"]
# 组装每个省份的却总人数为元组，并且各个省的数据都封装入列表内
date_list = []
for province_data in province_data_list:
    province_name = province_data["name"]
    province_confirm = province_data["total"]["confirm"]
    date_list.append((province_name+"省", province_confirm))
# 创建地图对象
map = Map()
# 添加数据
map.add("中国疫情确诊人数", date_list, "china")
# 设置全局变量，定制分段视觉映射
map.set_global_opts(
    title_opts=TitleOpts(title="中国各省确诊人数",pos_bottom="1%",pos_left="center"),
    visualmap_opts = VisualMapOpts(
        is_show=True, #是否显示
        is_piecewise=True, # 是否分段
        pieces=[
            {"min": 1, "max": 99, "label": "1-99", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "100-999", "color": "#FF6666"},
            {"min": 1000, "max": 2000, "label": "1000-2000", "color": "#990033"},
            {"min": 2001, "max": 5000, "label": "2001-5000", "color": "#990033"},
            {"min": 5001, "label": "5000以上", "color": "#990033"}
        ]
    )
)
# 绘图
map.render("全国疫情地图.html")
