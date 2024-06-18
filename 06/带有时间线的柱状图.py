from pyecharts.charts import Bar,Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType
# 建立好图表
bar1 = Bar()
bar1.add_xaxis(["中国","美国","俄罗斯"])
bar1.add_yaxis("GDP",[50,60,20],label_opts=LabelOpts(position="right"))
bar1.reversal_axis() # 翻转x轴
bar2 = Bar()
bar2.add_xaxis(["中国","美国","俄罗斯"])
bar2.add_yaxis("GDP",[70,90,30],label_opts=LabelOpts(position="right"))
bar2.reversal_axis()
bar3 = Bar()
bar3.add_xaxis(["中国","美国","俄罗斯"])
bar3.add_yaxis("GDP",[60,80,30],label_opts=LabelOpts(position="right"))
bar3.reversal_axis()
# 构建时间线对象
time_line = Timeline({"theme":ThemeType.LIGHT}) # 主题在构建时间线对象的时候添加就行了
time_line.add(bar1,"点1")
time_line.add(bar2,"点2")
time_line.add(bar3,"点3")

# 自动播放设置
time_line.add_schema(
    play_interval=1000, # 间隔时间，单位是毫秒
    is_timeline_show=True, # 是否显示时间线
    is_auto_play=True, # 是不是自动播放
    is_loop_play=True # 是不是循环播放
)
# 绘图
time_line.render("带有时间线的柱状图.html")