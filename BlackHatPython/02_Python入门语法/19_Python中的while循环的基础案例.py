import random

num = random.randint(1,100)
flag = True
i = 0
while flag:
    guess_num =  int(input("请输入你猜测的数字"))
    i += 1
    if guess_num == num:
        print(f"猜中了")
        flag = False
    else:
        if guess_num<num:
            print(f"猜错了小了 {num - guess_num}")
        else:
            print(f"猜错了 大了 {guess_num - num}")
print(f"你一共猜了{i}次")



















