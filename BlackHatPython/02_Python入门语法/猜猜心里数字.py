nun = int(input("请输入第一次猜想的数字："))

if nun == 10:
    print("恭喜你猜对了！")
elif  int(input("不对，再猜一次：")) == 10:
    print("恭喜你第二次猜对了")
elif int(input("不对，再猜一次：")) == 10:
     print("恭喜你第三次猜对了")
else:
    print("Sorry,全部猜错啦，我想的是10")