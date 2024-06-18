import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts
# 打开文件读取文件
f_us = open("D:\BaiduNetdiskDownload\资料\第1-12章资料\资料\资料\可视化案例数据\折线图数据\美国.txt",
            mode="r", encoding="utf-8"
            )
us = f_us.read()

f_jp = open("D:\BaiduNetdiskDownload\资料\第1-12章资料\资料\资料\可视化案例数据\折线图数据\日本.txt",
            mode="r", encoding="utf-8"
            )
jp = f_jp.read()

f_in = open("D:\BaiduNetdiskDownload\资料\第1-12章资料\资料\资料\可视化案例数据\折线图数据\印度.txt",
            mode="r", encoding="utf-8"
            )
indu = f_in.read()
# 把json格式外的内容删掉
us_data = us.replace("jsonp_1629344292311_69436(","")
jp_data = jp.replace("jsonp_1629350871167_29498(","")
in_data = indu.replace("jsonp_1629350745930_63180(","")
us_data = us_data[:-2]
jp_data = jp_data[:-2]
in_data = in_data[:-2]
# 把json的表格内容转化为字典
us_data = json.loads(us_data)
jp_data = json.loads(jp_data)
in_data = json.loads(in_data)
# 取到每个国家的趋势哪一项
us_trend = us_data["data"][0]["trend"]
jp_trend = jp_data["data"][0]["trend"]
in_trend = in_data["data"][0]["trend"]
# 拿到每个国家x和y轴的数据
us_x_data = us_trend["updateDate"][:314]
us_y_data = us_trend["list"][0]["data"][:314]
jp_x_data = jp_trend["updateDate"][:314]
jp_y_data = jp_trend["list"][0]["data"][:314]
in_x_data = in_trend["updateDate"][:314]
in_y_data = in_trend["list"][0]["data"][:314]

# 构建折线图对象
line = Line()

# 创建x轴
line.add_xaxis(us_x_data) # x轴都一样用一个就行了

# 创建y轴
line.add_yaxis("美国确诊人数", us_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数", jp_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数", in_y_data, label_opts=LabelOpts(is_show=False))
# label_opts控制数据的显示

# 设置全局变量
line.set_global_opts(
    title_opts = TitleOpts(title="2020年美日印三国确诊人数",pos_left="center",pos_bottom="1%")
)

# 生成图表
line.render()

# 关闭文件
f_us.close()
f_jp.close()
f_in.close()