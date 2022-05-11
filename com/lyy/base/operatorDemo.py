# 常用运算符

# + - * / %
# ** 幂，返回x的y次幂
print(2**8)                         # 256

# // 取整除，返回商的整数部分
print(8/3)                          # 2.6666666666666665
print(8//3)                         # 2
print()

# 比较运算符 == != > < >= <=

# 赋值运算符 = += -= *= /= %= **= //=

# 逻辑运算 and or not
# and会将左右两个表达式连接
print(3 > 8 and 3 < 2 or 3 > 1)     # True
print((3 > 8 and 3 < 2) or 3 > 1)   # True
print(3 > 8 and (3 < 2 or 3 > 1))   # False
print(3 > 1)                        # True
print(not 3 > 1)                    # False
print()

# 成员运算符 in 和 not in
# 可以用来测试字符串、列表、元组、字典、集合，但是不能测试数字类型
nameList = ["lyy", "lly", "gx", "xqj"]
print("lyy" in nameList)            # True
print("dt" in nameList)             # False
print("dt" not in nameList)         # True