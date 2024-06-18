from pyecharts.charts import Bar,Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import LabelOpts
f = open("1960-2019全球GDP数据.csv", mode="r",encoding="GBK")
a = f.readline() # 把第一行读取了
year = []
country = []
gdp = []
for item in f.readlines():
    item = item.strip().split(",") # 把每行的字符串通过“,”隔开转化成列表
    year.append(item[0])
    country.append(item[1])
    gdp.append(item[2])
# 每个柱状图8个国家就行了
start = 0
end = 8
time_line = Timeline({"theme": ThemeType.LIGHT})
for i in range(len(year)//8):
    c = country[start:end]
    g = gdp[start:end]
    bar = Bar()
    bar.add_xaxis(c)
    bar.add_yaxis("GPD", g, label_opts=LabelOpts(position="right"))
    bar.reversal_axis()
    time_line.add(bar, year[end]+"GDP")
    start += 8
    end += 8
time_line.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_loop_play=True,
    is_auto_play=True
)
time_line.render()