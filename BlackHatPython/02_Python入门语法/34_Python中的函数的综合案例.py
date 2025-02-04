from fileinput import close
# 查询余额
def AskMoney(name):
    global money
    print(f"{name},您好，您的余额剩余：{money} 元")
# 存款
def SaveMoney(name,s):
    print(f"{name} 你好，你存款{s}元成功")
    global money
    money = money + s
    print(f"{name} 你好，你的余额剩余：{money}元")
# 取款
def TakeMoney(name,t):
    print(f"{name},你好，您取出{t}元成功")
    global money
    money = money - t
    print(f"{name} 你好，你的余额剩余：{money}元 ")
# 退出
def exit():
    close()
# 主菜单函数
def menu():
    (print
     (f"""  _______主菜单_______
     {name},您好，欢迎来到黑马银行ATM，请选择操作：
     查询余额\t[输入1]
     存款\t\t[输入2]
     取款\t\t[输入3]
     退出\t\t[输入4]
    """))
    while True:
        UserX = int(input("请输入你的选择："))
        if UserX == 1:
            AskMoney(name)
        elif UserX == 2:
            save_money = int(input("请输入你存款的数额："))
            SaveMoney(name, save_money)
        elif UserX == 3:
            take_money = int(input("请输入你取款的数额："))
            TakeMoney(name, take_money)
        elif UserX == 4:
            break
        else:
            break
money = 5000000
name = input("请输入您的名字")
menu()







