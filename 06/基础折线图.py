# 导入pyecharts包
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts
# 创建一个折线图对象
line = Line()
# 给折线图对象添加x轴的数据(x轴只能传数据，不可以命名)
line.add_xaxis(["中国","美国","俄罗斯"])
# 给折线图对象添加y轴的数据
line.add_yaxis("GDP",[120, 100, 80])
# 设置全局配置项
line.set_global_opts(
    title_opts = TitleOpts(title="GDP展示",pos_left="center",pos_bottom="1%"),# 控制标题
    legend_opts= LegendOpts(is_show= True),# 控制图列
    toolbox_opts= ToolboxOpts(is_show= True), # 控制工具箱
    visualmap_opts= VisualMapOpts(is_show= True) # 控制视觉映射
)
# 通过render的方法将代码生成图像
line.render()