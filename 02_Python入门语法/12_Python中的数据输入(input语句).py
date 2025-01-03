"""
演示Python的input语句
获取键盘的输入信息
input默认接收数据类型是字符串 string
"""
print("请告诉我你是谁？")
name = input()
print("我知道了，你是： %s" %name)

"""方式二
name=input("请告诉我你是谁？")
print("我知道了，你是： %s" %name)
"""
# 输入数字类型
num=input("请告诉我你的银行卡密码：")
# 数据类型转换
num = int(num)
print("你的银行卡密码的类型是：",type(num))