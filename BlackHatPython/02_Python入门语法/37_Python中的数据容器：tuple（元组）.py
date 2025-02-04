# 定义元组
t1 = (1,"Heillo",True)
t2 = ()
t3 = tuple()
print(f"t1的类型是：{type(t1)},内容是：{t1}")
print(f"t2的类型是：{type(t2)},内容是：{t2}")
print(f"t3的类型是：{type(t3)},内容是：{t3}")

# 定义单个元素的元素
t4 = ("Hello",)
print(f"t4的类型是：{type(t4)},内容是：{t4}")

# 元组的嵌套
t5 = ((1,2,3),(4,5,6))
print(f"t5的类型是：{type(t5)},内容是：{t5}")

# 元组的操作：index查找方法
t6 = ("教育","黑马程序员","Python")
index = t6.index("黑马程序员")
print(f"在元组t6中查找黑马程序员的下标是：{index}")

# 元组的操作：count统计方法
t7 = ("教育","黑马程序员","Python","黑马程序员","黑马程序员","Python")
mun = t7.count("黑马程序员")
print(f"在元组t7中统计黑马那程序员的数量有：{mun}")

# 元组的操作：len函数统计元组元素数量
t8 = ("教育","黑马程序员","Python","黑马程序员","黑马程序员","Python")
mun = len(t8)
print("t8元组中的元素有：5个")

# 元组的遍历：while
index = 0
while index < len(t8):
    print(f"元组的元素有：{t8[index]}")
    index += 1
# 元组的遍历：for
for x in t8:
    print(f"元组的元素有{x}")

# 修改元组内容
# t8[0] = "itcast"

# 定义一个元组
t9 = (1,2,["itheima","itcast"])
print(f"t9的内容是：{t9}")
t9[2][0] = "黑马程序员"
t9[2][1] = "传智教育"
print(f"t9的内容是：{t9}")