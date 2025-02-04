# 列表的定义
# 定义一个列表list
# my_list = ["itheima", "itcast", "python"]
# print(my_list)
# print(type(my_list))
#
# my_list = ["itheima", 666, True]
# print(my_list)
# print(type(my_list))
#
# # 定义一个嵌套的列表
# my_list = [[1, 2, 3], [4, 5, 6]]
# print(my_list)
# print(type(my_list))

# 通过下标索引取出对应位置的数据
# my_list = ["Tom","lily","Rose"]
# # 列表[  下标索引 ] ，从前向后从0开始，每次+1            从后向前从-1开始，每次-1
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[-1])
# print(my_list[-2])
# print(my_list[-3])

# 取出嵌套列表的元素
# my_list = [ [ 1, 2, 3 ] , [ 4, 5, 6 ] ]
# print(my_list[1][1])
mylist = [ "itcast","itheima","python" ]
# 1.1 查找某元素在列表内的下标索引
index = mylist.index("itheima")
print(f"itheima在列表中的下标索引值是：{index}")

# 1.2如果被查找的元素不存在，会报错
# index = mylist.index("Hello")
# print(f"Hello在列表中的下标索引值是：{index}")

# 2. 修改特定下标索引的值
mylist[0] = "智慧教育"
print(f"列表被修改元素值后，结果是：{mylist}")

# 3.在指定下标位置插入新元素
mylist.insert(1,"best")
print(f"列表插入元素后，结果是：{mylist}")

# 4. 在列表的尾部追加
mylist.append("黑马程序员")
print(f"列表在追加了元素后，结果是：{mylist}")

# 5. 在列表的尾部追加‘’‘一批’‘’新元素
mylist2 = [1,2,3]
mylist.extend(mylist2)
print(f"列表再追加了一个新的列表后，结果是：{mylist}")

# 6. 删除指定下标索引的元素（两种方式）
mylist = [ "itcast","itheima","python" ]
# 6.1方式1：del 列表[下标]
del mylist[2]
print(f"列表删除元素后，结果是：{mylist}")

# 6.2 方式2：列表.pop（下标）
mylist = [ "itcast","itheima","python" ]
element = mylist.pop(2)
print(f"通过pop方法取出元素后列表内容：{mylist},去除的元素是：{element}")

# 7. 删除某元素在列表中的第一个匹配项
mylist = [ "itcast","itheima","itcast","itheima","python" ]
mylist.remove("itheima")
print(f"通过remove方法移除元素后，列表的结果是：{mylist}")

# 8. 清空列表
mylist.clear()
print(f"列表被清理了，结果是：{mylist}")

# 9. 统计列表内某元素的数量
mylist = [ "itcast","itheima","itcast","itheima","python" ]
count = mylist.count("itheima")
print(f"列表中itheima的数量是：{count}")

# 10. 统计列表中全部的元素数量
mylist = [ "itcast","itheima","itcast","itheima","python" ]
count = len(mylist)
print(f"列表的元素数量总共有 {count} 个")


























