# 循环10次
# 0 1 2 3 4 5 6 7 8 9
for i in range(10):
    print(i, end=' ')   # 指定print最后以' '结束，默认以'\n'结束
print("\n")
# 此时i保留了最后一次的值
print(i)                # 9 
print('\n')

# 该语法中in后面跟数据的集合
# lyy lly gx xqj
nameList = ["lyy", "lly", "gx", "xqj"]
for name in nameList:
    print(name, end=' ')
print('\n')

# H e l l o   w o r l d !
for leter in "Hello world!":
    print(leter, end=' ')
print('\n')

# range([开始], [结束], [步长])
# 5 7 9 11 13 15 17 19
for i in range(5, 20, 2):
    print(i, end=' ')
print('\n')

# 10 9 8 7 6
for i in range(10, 5, -1):
    print(i, end=' ')
print('\n')

for floor in range(1, 7):
    if floor == 3:
        continue            # 停止当前该次循环
    print(f"floor:{floor}")
    for room in range(1, 5):
        if floor == 4 and room == 4:
            break           # 直接跳出当前循环
        print(f"room:{floor}0{room}")

# 打印九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{i}x{j}={i*j}", end=' ')
    print()

# 打印三角形
for i in range(11):
    if i <= 5:
        print('*' * i)
    else:
        print('*' * (10-i))