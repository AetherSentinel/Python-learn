def CheckHealth(b):
    print(f"欢迎来到黑马程序员！请出示您的健康码以及七十二小时核酸证明，并配合测量体温！")
    if int(b) <=  37.5:
        print(f"体温测量中，您的体温是：{b} ,体温正常请进")
    else:
        print(f"体温测量中，您的体温是：{b} ,需要隔离")
a =input("")
CheckHealth(a)