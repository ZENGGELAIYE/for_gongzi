def str_reverse(s):
    # s = reversed(s)
    # a = list(s)
    a = s[::-1]
    return a

def substr(s, x):
    s = s.split(x)
    return s

if __name__ == '__main__': # 是为了在模块中测试代码是否可以正常运行
    a = str_reverse("你知道我在等你吗？")
    print(a)