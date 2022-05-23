# for...else...语法
# while同样适用
for i in range(5):
    print(i)
else:
    print("完整循环完成才进入else部分")

for i in range(5):
    print(i)
    if i == 4:
        break
else:
    print("完整循环完成才进入else部分")