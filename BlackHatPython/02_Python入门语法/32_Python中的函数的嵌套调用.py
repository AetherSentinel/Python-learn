def func_b():
    print("___2___")
# 定义函数func_a ,并在内部调用func_b
def func_a():
    print("___1___")
    # 嵌套调用func_b
    func_b()
    print("___3___")
# 调用函数func_a
func_a()
