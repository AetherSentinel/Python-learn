CEO_money = int(10000)
for yg in range(1,21):
    import random
    performance = random.randint(1,10 )
    if performance < 5:
         print(f"员工 {yg} ，绩效分：{performance} , 低于5，不发工资，下一次位")
         continue
    if CEO_money >= int(1000):
         print(f"员工 {yg}  绩效分：{performance} 发放工资{int(1000)}元，账户余额还剩余{CEO_money - int(1000)} 元")
         CEO_money -= int(1000)
    else:
        print(f"工资发完了，下个月领取把")
        break
