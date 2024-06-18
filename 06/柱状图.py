from pyecharts.charts import Bar
from pyecharts.options import TitleOpts,LabelOpts
bar = Bar()
bar.add_xaxis(["中国", "美国", "俄罗斯"])
bar.add_yaxis("GDP", [30, 20,10],label_opts=LabelOpts(position="right"))
bar.add_yaxis("GDP1", [20, 50,20],label_opts=LabelOpts(position="right"))
bar.reversal_axis()
bar.render("柱状图.html")