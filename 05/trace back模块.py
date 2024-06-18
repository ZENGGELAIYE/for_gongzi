import traceback
import logging
# try:
#     print(1/0)
# except:
#     print("程序出错了")
#     print(traceback.format_exc())
#     # 这样的话程序就会把报错的内容弹出来

logging.basicConfig(
    filename ='chucuo.txt',
    format ='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s',
    datefmt ='%Y-%m-%d %H:%M:%S',
    level = 40) # 记录文件中的日志的最低等级

try:
    print(1/0)
except:
    print("程序出错了")
    logging.error(traceback.format_exc())
