FirstList = [1,2,3,4,5,6,7,8,9,10]
SecondList = []

# While 例子
element = 0
while element < len(FirstList):
    if FirstList[element] % 2 == 0:
        SecondList.append(FirstList[element])
    element +=1

print(f"通过while循环，从列表：{FirstList} 中取出偶数，组成新列表：{SecondList}")

SecondList = [] #初始化列表
print(f"初始化成功 SecondList ：{SecondList}")

for element in FirstList:
    if element % 2 ==0:
        SecondList.append(element)

print(f"通过for循环，从列表：{FirstList} 中取出偶数，组成新列表：{SecondList}")