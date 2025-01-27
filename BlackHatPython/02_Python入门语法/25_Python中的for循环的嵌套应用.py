"""
课后作业 用for写一个乘法表
"""
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i} * {j} = {i * j}\t", end="")
    print()

# i=1
# for i in range(1,101):
#     print(f"这是我坚持表白的第 {i} 天")
#
#     for j in range(1,11):
#         print(f"送给小妹的第 {j}朵小红花")
#     print(f"小妹这是我表白的第{i}天结束")
#
# print(f"第{i} 天表白成功")
#

# i = 1
# while i<=100:
#     print(f"这是我坚持表白的第 {i} 天")
#     for j in range(1,11):
#         print(f"送给小妹的第 {j}朵小红花")
#     print(f"小妹这是我表白的第{i}天结束")
#     i += 1
# print(f"第{i-1} 天表白成功")