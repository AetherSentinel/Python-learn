MyStr = "itheima itcst boxuegu"
Value_IT = MyStr.count("it")
NweMyStr = MyStr.replace(" ","|")
MyStrList = NweMyStr.split("|")

print(f"字符串{MyStr}中有：{Value_IT} 个it字符串")
print(f"字符串{MyStr}，被替换空格后，结果：{NweMyStr}")
print(f"字符串{MyStr}，按照 | 分隔后，得到{MyStrList}")