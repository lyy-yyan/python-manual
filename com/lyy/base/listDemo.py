# list 列表类似其他语言中的数组
nameList = ["lyy", "lly", "gx", "xqj"]      # 创建列表
print(type(nameList))   # 查看类型
print(nameList)
print(nameList[0])      # 取出某个值

# 遍历列表
for name in nameList:
    print(f"name: {name}")

# 增加元素
nameList.append("dt")
print(nameList)

# 插入元素 
# 参数 (要插入位置, 插入元素)
nameList.insert(2, "cr")
print(nameList)

# 修改元素
nameList[0] = "lyyyyy"
print(nameList[0])

# 查询元素
print(nameList.index("dt"))
# print(nameList.index("xxx"))      # 查询不存在的值会报错

# 删除元素
del nameList[5]         # 通过序号删除
print(nameList)
nameList.remove("cr")   # 通过内容删除
print(nameList)

# 列表切片
print(nameList[:2])
print(nameList[-3:-1])  # 可以用负序号取元素
print(nameList[0::2])   # 按固定步长取元素[头:尾:步长]

# 嵌套
nameList.append(["lyy", "lly"])
print(nameList)
print(nameList[4][0])