# 设计一个类完成数据的封装
# 设计一个抽象类，定义文件的读取相关功能，并使用子类实现具体功能
# 读取文件，生产数据对象
# 进行数据需求的逻辑计算(计算每一天的销售额)
# 通过pyedhart进行绘图
from file_define import File_Record,TextFileRead,Json_File_Read
from date_define import Record
from pyecharts.charts import Bar,Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType
textfileread = TextFileRead("D:/BaiduNetdiskDownload/资料/第13章资料/2011年1月销售数据.txt")
jsonfileread = Json_File_Read("D:/BaiduNetdiskDownload/资料/第13章资料/2011年2月销售数据JSON.txt")
jan_data : list[Record]= textfileread.read_data()
feb : list[Record]= jsonfileread.read_data()
# 将两个月份的数据合并为一个list来储存
all_data : list[Record]= jan_data + feb
data_dict = {}
for record in all_data:
    if record.date in data_dict.keys():
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money
print(data_dict)
# 动态，五天一页
timeline = Timeline({"theme":ThemeType.LIGHT})
data_keys = sorted(data_dict.keys())
print(data_keys)
x = 0
y = 5
for a in range(len(data_keys)//5 + 1):
    bar = Bar()
    x_date = []
    y_date = []
    for data in data_keys[x:y]:
        x_date.append(data)
        y_date.append(data_dict[data])
    bar.add_xaxis(x_date)
    bar.add_yaxis("money",y_date,label_opts=LabelOpts(position="top"))
    try:
        timeline.add(bar,data_keys[x] + "-" + data_keys[y])
    except:
        timeline.add(bar, data_keys[x] + "-" + data_keys[-1])
    x += 5
    y += 5
timeline.add_schema(
    play_interval=1000,
    is_loop_play=True,
    is_auto_play=True,
    is_timeline_show=True
)
timeline.render("大的来了.html")