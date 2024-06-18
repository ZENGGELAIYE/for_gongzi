from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts,TitleOpts
from pyecharts.globals import ThemeType
# 读取数据
f = open("1960-2019全球GDP数据.csv",mode="r",encoding="GBK")
date = f.readlines()
# 关闭文件
f.close()
# 删除第一条数据
date.pop(0)
# 将数据转化为字典储存，格式为
date_dict = {}
for item in date:
    item = item.split(",")
    year = int(item[0])
    country = item[1]
    gdp = float(item[2])
    try:
        date_dict[year].append([country,gdp])
    except KeyError:
        date_dict[year] = [[country,gdp]]
# 排序年份
year_data = sorted(date_dict.keys()) # 可以把字典变成列表
time_line = Timeline({"theme": ThemeType.LIGHT}) # 先在循环外面把time_line给设置好
# 创建时间线对象
for year in year_data:
    date_dict[year].sort(key=lambda item : item[1], reverse=True)
    country = []
    gdp = []
    for cy in date_dict[year][0:8]:
        country.append(cy[0])
        gdp.append(cy[1]//100000000)
    bar = Bar()
    country.reverse() # 直接将列表进行翻转一下
    gdp.reverse() # 翻转一下
    bar.add_xaxis(country)
    bar.add_yaxis("GDP(万亿)", gdp,label_opts=LabelOpts(position="right"))
    bar.reversal_axis()
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球GDP前八的国家")
    ) # 要设置标题的话，必须在timeline之前
    time_line.add(bar,year)
time_line.add_schema(
    play_interval= 1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)
time_line.render()


# for循环每一年的数据，基于每一年的数据，创建每一年的bar对象
# 设置时间线自动播放