# 数据类型

age = 13

# 查看变量内存地址
print(id(age))

# 查看变量类型
print(type(age))                # <class 'int'>
# python3之后不再有long数据类型

# 字符串' ' or " " or ''' '''（用于多行字符串）
name = "lyyyyy"
msg = '''
hello, 
this is a Multi-line message.'''
print(msg)
print(type(name))               # <class 'str'>
print(name[1])                  # 可索引
# name[1] = "w"                 # 会报错，字符串不可修改
print(name[1:3])                # 可切片，“顾头不顾尾”

# 字符串的一些方法
print(name.capitalize())        # Lyyyyy
print(name.upper())             # LYYYYY
print(name.center(20, "-"))     # -------lyyyyy-------
print(msg + "\n--" + name)      # 字符串拼接

# 字符串内引用外部变量
# python3之前的方法
end = ''.center(20, '-')
card = '''%s
name: %s
age: %d
%s
''' % (name.center(20, "-"), name[:3], age, end)
print(card)
# 更方便：python3之后的方法
card = f'''{name.center(20, "-")}
name: {name[:3]}
age: {age}
{end}
'''
print(card)
# 输出
# -------lyyyyy-------
# name: lyy
# age: 13
# --------------------