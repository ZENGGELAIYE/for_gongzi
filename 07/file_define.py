"""
和文件相关的类都在这里
"""
from date_define import Record
import json
# 先定义一个抽象类来做顶层设计，确定有哪些功能需要实现
class File_Record:
    def read_data(self) -> list[Record]:
        """读取文件的数据，读取到的每一条数据都转换为Record对象，将他们封装到list里面即可"""
        pass

class TextFileRead(File_Record):
    def __init__(self,path):
        self.path = path # 定义成员变量记录文件路径
    def read_data(self) -> list[Record]:
        f = open(self.path,mode="r",encoding="utf-8")
        file_data = f.readlines()
        f.close()
        record_list : list[Record] = []
        for line in file_data:
            line = line.strip()
            line = line.split(",")
            record = Record(line[0],line[1],int(line[2]),line[3])
            record_list.append(record)
        return record_list
class Json_File_Read(File_Record):
    def __init__(self,path):
        self.path = path # 定义成员变量记录文件路径
    def read_data(self) -> list[Record]:
        f = open(self.path,mode="r",encoding="utf-8")
        file_data = f.readlines()
        record_list : list[Record] = []
        for line in file_data:
            line_dict = json.loads(line) # 这种是CSV格式的必须每排的来读取
            record = Record(line_dict["date"],line_dict["order_id"],int(line_dict["money"]),line_dict["province"])
            record_list.append(record)
        return record_list




if __name__ == '__main__':
    textfileread = TextFileRead('D:/BaiduNetdiskDownload/资料/第13章资料/2011年1月销售数据.txt')
    list1 = textfileread.read_data()
    jsonfileread = Json_File_Read('D:/BaiduNetdiskDownload/资料/第13章资料/2011年2月销售数据JSON.txt')
    list2 = jsonfileread.read_data()
    for i in list1:
        print(i)
    for l in list2:
        print(l)