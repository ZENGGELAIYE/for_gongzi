import logging
# filename: 文件名
# format: 数据的格式化输出。最终在文件中的样子
#        时间-名称-级别-模块：错误信息
# datefmt: 时间的格式
# # level: 错误的级别权重，当错误的级别权重大于等于level的时候才会写入文件
# logging.basicConfig(
#     filename ='filename.txt',
#     format ='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s',
#     datefmt ='%Y-%m-%d %H:%M:%S',
#     level = 40) # 记录文件中的日志的最低等级
#
# logging.critical("今天程序爆炸了，我找程序员来保修") # 最高级别日志信息 50
# logging.error("一般指的是普通程序报错，俗称bug") # 40
# logging.warning("我只是一个警告信息") # 30
# logging.info("我只是一个普通信息") # 20
# logging.debug("默认最低等级的信息") # 10

# 创建多个日志
file_handler = logging.FileHandler('FILE1.LOG','a',encoding='utf-8') # f = oppen(文件名，写入模式，encoding)
file_handler.setFormatter(logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s'))

logger1 = logging.Logger('财务系统',level=40) # 创建日志对象
logger1.addHandler(file_handler) # 给日志对象设置文件信息

logger1.error("我是A系统")

file_handler = logging.FileHandler('FILE2.LOG','a',encoding='utf-8') # f = oppen()
file_handler.setFormatter(logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s'))

logger2 = logging.Logger('会计系统',level=40) # 创建日志对象
logger2.addHandler(file_handler) # 给日志对象设置文件信息

logger2.error("我是B系统")