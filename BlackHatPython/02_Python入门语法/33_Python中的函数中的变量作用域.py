# 演示局部变量
# def test_a():
#     num = 100
#     print(num)
#
# test_a()
# 除了函数体，局部变量就无法使用

# 演示全局变量
# num = 200
# def tast_a():
#     print(f"test_a:{num}")
#
# def tast_b():
#     print(f"test_a:{num}")
# tast_a()
# tast_b()
# print(num)

# 在函数内修改全局变量
num = 200
def tast_a():
    print(f"test_a:{num}")

def tast_b():
    # global 关键字声明a是全局变量
    global num          # 设置内部定义的变量为全局变量
    num = 500
    print(f"test_a:{num}")
tast_a()
tast_b()
print(num)