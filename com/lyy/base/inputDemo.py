# 读取用户指令
import msilib

name = input("your name:")

# input()接收的结果都是字符串类型的
# 想要age作为int类型需做强制转换
age = input("your age:")
if age.isdigit():                   # 判断字符串是否为数字
    age = int(age)
else:
    print("error: The input is not an int.")
    exit()                          # 退出程序

job = input("your job:").strip()    # strip()可跳过输入的空格制表符等
end = ''.center(20, '-')

card = f'''
{name.center(20, "-")}
name: {name[:3]}
age: {age}
job: {job}
{end}
'''
print(card)
# --------lyy---------
# name: lyy
# age: 14
# job: a
# --------------------

print(type(name))                   # <class 'str'>
print(type(age))                    # <class 'int'>