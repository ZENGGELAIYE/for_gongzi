
def func():
    a = 20  # 每次执行func函数a的值会被刷新吗？
    def anc():
        nonlocal a
        a += 20
        return a
    return anc()
func()
func()
# 我这里执行了两次func函数a还是40
print(func())