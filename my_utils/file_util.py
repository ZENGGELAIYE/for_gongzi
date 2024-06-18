def print_file_info(file_name):
    """
    打印一个文件
    :param file_name: 文件的路劲
    :return: None
    """
    a = None
    try:
        a = open(file_name, mode="r", encoding="utf-8")
        for item in a:
            print(item.strip())
    except Exception as b:
        print(f"出现错误了，错误是{b}")
    finally:
        if a:
            a.close()

def append_to_file(file_name, data): # data也是一个文件
    b = open(file_name, mode="wb")
    c = open(data, mode="rb")
    for line in c:
        b.write(line)
    b.close()
    c.close()
    d = open(file_name, mode="rb")
    print(d.readlines())

if __name__ == '__main__': # 是为了在模块中测试代码是否可以正常运行
    print_file_info("file_name")