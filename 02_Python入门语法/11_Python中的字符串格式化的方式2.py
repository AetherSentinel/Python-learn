# 演示第二种字符串格式化的方式：f{占位}

name = "博客"
ste_up_year = 2006
stock_price = 19.99
# f：format
print(f"我是{name}，我成立于：{ste_up_year}年，我今天的股价是：{stock_price}")

# 演示对表达式进行字符串格式化

print("1 * 1 的结果是：%d" % (1*1))
print(f"1 * 2 的结果是：{1*2}")
print("字符串在Python中的类型名是：%s" % type("字符串"))
