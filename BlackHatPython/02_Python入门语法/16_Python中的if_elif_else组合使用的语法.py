"""
演示if elif else多条件判断语句的使用
"""
# height = int(input("请输入你的身高（cm）："))
# vip_level = int(input("请输入你的VIP等级（1~5）："))
# day = int(input("请告诉我今天几号（1~30）："))
# 通过if判断，可以使用多条件判断的语法
# 第一个条件就是if
if int(input("请输入你的身高（cm）：")) < 120:
    print("身高小于12cm，可以免费")
elif int(input("请输入你的VIP等级（1~5）：")) > 3:
    print("vip级别大于3，可以免费")
elif int(input("请告诉我今天几号（1~30）：")) == 1:
    print("今天是一号免费日，可以免费")
else:
    print("不好意思，条件都不满足，需要购票")
print("祝您游玩愉快")