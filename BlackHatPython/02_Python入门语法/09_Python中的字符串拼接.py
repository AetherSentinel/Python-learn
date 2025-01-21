# 字符串字面量之间的拼接
print("学IT来黑马"+"月薪过万")
# 字符串字面量和字符串变量的拼接
name = "黑马程序员"
address = "建材城东路9号院子"
tel = 4006189090
str_tel = str(tel)
# 错误示范：print("我是：" +name +",我的地址是："+address+"，我的电话是："+tel)   tel是整数型不能直接print出来
print("我是：" +name +",我的地址是："+address+"，我的电话是："+str_tel)