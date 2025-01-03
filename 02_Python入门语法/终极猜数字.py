import random
num = random.randint(1,10)
guess = int(input("你第一次猜的数字是："))
if guess ==num:
    print("恭喜你第一次就猜对了")
else:
    if guess >num:
        print("与答案相比大了")
    else:
        print("与答案相比小了")
    guess = int(input("你第二次猜的数字是："))
    if guess == num:
        print("恭喜你第二次就猜对了")
    else:
        if guess > num:
            print("与答案相比大了")
        else:
            print("与答案相比小了")
        guess = int(input("你第三次猜的数字是："))
        if guess == num:
            print("恭喜你第三次就猜对了")
        else:
            print("猜错了！三次机会用完啦！")

# 老师案例
# import  random
# num = random.randint(1,10)
#
# guess_num = int(input("输入你要猜测的数字："))
#
# # 通过if判断语句进行数字的猜测
# if guess_num == num:
#     print("恭喜第一次就猜对了")
# else:
#     if guess_num >num:
#         print("你猜测的数字大了")
#     else:
#         print("你猜测的数字小了")
#
#     guess_num = int(input("再次输入你要猜测的数字："))
#
#     if guess_num == num:
#         print("恭喜第二次猜中了")
#     else:
#         if guess_num > num:
#             print("你猜测的数字大了")
#         else:
#             print("你猜测的数字小了")
#         guess_num = int(input("第三次输入你要猜测的数字："))
#         if guess_num == num:
#             print("恭喜你第三次猜中了")
#         else:
#             print("三次机会用完了 ，没有猜中")
