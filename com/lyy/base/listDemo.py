# list 列表（类似其他语言中的数组）

from tarfile import XHDTYPE


nameList = ["lyy", "lly", "gx", "xqj"]      # 创建列表
print(type(nameList))                       # 查看类型
print(nameList)
print(nameList[0])                          # 取出某个值

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
# print(nameList.index("xxx"))              # 查询不存在的值会报错

# 删除元素
del nameList[5]                             # 通过序号删除
print(nameList)
nameList.remove("cr")                       # 通过内容删除
print(nameList)

# 列表切片
print(nameList[:2])
print(nameList[-3:-1])                      # 可以用负序号取元素
print(nameList[0::2])                       # 按固定步长取元素[头:尾:步长]

# 嵌套
nameList.append(["lyy", "lly"])
print(nameList)
print(nameList[4][0])

print(f"打印nameList:{nameList}")   # ['lyyyyy', 'lly', 'gx', 'xqj', ['lyy', 'lly']]
# 列表方法
## 增
nameList.append("lh")               # ['lyyyyy', 'lly', 'gx', 'xqj', ['lyy', 'lly'], 'lh']
nameList.insert(0, "lyy")           # ['lyy', 'lyyyyy', 'lly', 'gx', 'xqj', ['lyy', 'lly'], 'lh']

## 删除
## 清空 nameList.clear()
## 默认删除最后一个元素并返回 nameList.pop(), nameList.pop(-3)
## 删除指定的值（仅删除第一个）
nameList.remove("lyy")              # ['lyyyyy', 'lly', 'gx', 'xqj', ['lyy', 'lly'], 'lh']

## 删除整个变量
del nameList[-1]                    # ['lyyyyy', 'lly', 'gx', 'xqj', ['lyy', 'lly']]

# 切片
print(nameList[0:3])                # ['lyyyyy', 'lly', 'gx']
print(nameList[0::2])               # ['lyyyyy', 'gx', ['lyy', 'lly']]
print(nameList[-3:])                # ['gx', 'xqj', ['lyy', 'lly']]
## 反转
print(nameList[::-1])               # [['lyy', 'lly'], 'xqj', 'gx', 'lly', 'lyyyyy']
## 也可以使用 反转函数 nameList.reverse()

# 查询
print("lyy" in nameList)            # False
## 计数
print(nameList.count('gx'))         # 1
print(nameList.index('gx'))         # 2

nums = [1, 5, 20, 9, 10]
# 正序排序
nums.sort()
print(nums)                         # [1, 5, 9, 10, 20]
# 倒序排序
nums.sort(reverse=True)             
print(nums)                         # [20, 10, 9, 5, 1]

nameList.extend(nums)
print(nameList)                     # ['lyyyyy', 'lly', 'gx', 'xqj', ['lyy', 'lly'], 20, 10, 9, 5, 1]

# 浅copy
names = nameList.copy()
print(names)                        # ['lyyyyy', 'lly', 'gx', 'xqj', ['lyy', 'lly'], 20, 10, 9, 5, 1]

# 引用的是同一个地址
print(id(names[4]) == id(nameList[4]))  # True

names[0] = "lyy"
print(names)                        # ['lyy', 'lly', 'gx', 'xqj', ['lyy', 'lly'], 20, 10, 9, 5, 1]
print(nameList)                     # ['lyyyyy', 'lly', 'gx', 'xqj', ['lyy', 'lly'], 20, 10, 9, 5, 1]

names[4][1] = "xh"
print(names)                        # ['lyy', 'lly', 'gx', 'xqj', ['lyy', 'xh'], 20, 10, 9, 5, 1]
print(nameList)                     # ['lyyyyy', 'lly', 'gx', 'xqj', ['lyy', 'xh'], 20, 10, 9, 5, 1]

# 对于内部引用，copy的只是地址，其中一个修改，另一个也会被修改

# 深copy
import copy
names = copy.deepcopy(nameList)
print(id(names[4]) == id(nameList[4]))  # False

# 列表生成式
list = [f"staff-{i}" for i in range(1, 10)]
print(list)     # ['staff-1', 'staff-2', 'staff-3', 'staff-4', 'staff-5', 'staff-6', 'staff-7', 'staff-8', 'staff-9']