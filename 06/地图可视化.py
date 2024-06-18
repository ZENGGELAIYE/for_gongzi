from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
# 准备地图对象
map = Map()
# 准备数据
data = [("北京市",99), ("上海市", 199), ("四川省", 299), ("广东省", 399),("浙江省", 499)]
# 添加数据
map.add("中国地图", data, "china")
# 导入全局变量
map.set_global_opts( # 这个是搞图列的
    visualmap_opts=VisualMapOpts(
        is_show=True,  # 是否显示
        is_piecewise=True, # 是否分段
        pieces =[
            {"min":1, "max":9, "label":"1-9", "color": "#CCFFFF"},
            {"min":10, "max":99, "label":"10-99", "color": "#FF6666"},
            {"min":100, "max":500, "label":"100-500", "color": "#990033"}
        ]

    )
)
# 绘图
map.render()
# 设置全局选项