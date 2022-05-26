# 深入了解字符串
## 字符串定义
    # 1. 字符串是由0个或多个字符组成的有限序列
    # 2. 不可变、有索引、可切片、可遍历

## 字符串是对象

# 查看方法手册：help(s.expandtabs)，q退出
## 字符串类型方法

 # 1. 格式化方法
# 首字母大写
from encodings import utf_8
from unicodedata import name


"jack".capitalize()             # 'Jack'
# 都转换成小写方便比较
"jack" == "Jack"                # 'False'
"Jack".casefold()               # 'jack'
# 两边填充
"jack".center(30, '-')          # '-------------jack-------------'
# 自动转换Tab（制表符）
print("a\tb")                   # 'a       b'
"a\tb".expandtabs(1)            # 'a b'
# 左(右)对齐，往右(左)填充
"jack".ljust(30, '-')           # 'jack--------------------------'
"jack".rjust(30, '-')           # '--------------------------jack'
# 全转换小写
"Jack".lower()                  # 'jack'
# 大小写互换
"Jack".swapcase()               # 'jACK'
# 所有单词首字母大写
"my love".title()               # 'My Love'
# 全部改为大写
"jack".upper()                  # 'JACK'
# 无字符的地方填0
"my love".zfill(30)             # '00000000000000000000000my love'
# 去除两边(左/右)的\0 \t \n等
" my love \n".strip()           # 'my love'
" my love \n".lstrip()          # 'my love \n'
" my love \n".rstrip()          # ' my love'
# format引用变量
s1 = "my love"
s2 = "jack"
f"{s1} is {s2}"                 # 'my love is jack'
"my name is {name}, my age is {age}".format(name='jack', age=13)     # 'my name is jack, my age is 13'
"my name is {0}, my age is {1}".format("lyy", 13)               # 'my name is lyy, my age is 13'
    
# 2. 判断方法
# 以什么开头，以什么结尾
"jack".startswith("j")          # True
"jack".startswith("J")          # False
"jack".endswith("k")            # True
# 是否都是字母，注意空格等字符
" my love".isalpha()            # False
"mylove".isalpha()              # True
# 是否字母或是数字
"age13".isalnum()               # True
# 是否数字
"22".isdigit()                  # True
"二十五".isnumeric()            # True
# 是否合法可做变量的名字
"lyy".isidentifier()            # True
"1".isidentifier()              # False
# 是否都是小写
"13lyy".islower()               # True
"Jack".islower()                # False
# 是否可打印
"lyy".isprintable()             # True
# 是否空格
' '.isspace()                   # True
# 是否标题
"The Title".istitle()           # True
"the title".istitle()           # False

# 3. 查、改、计数、替换
# 查找字符位置，找不到返回-1
"love lyy".find('l')            # 0
"love lyy".find('a')            # -1
"love lyy".find('l', 3, -1)     # 5
"love lyy".rfind('l')           # 5
# 返回字符位置，找不到报错
"love lyy".index('l')           # 0
# 计数
"love lyy".count('l')           # 2
"love lyy".count('l', 3, -1)    # 1
# 切割为列表
"love lyy".split()              # ['love', 'lyy']
"love lyy".split('l')           # ['', 'ove ', 'yy']
"lo ly ly l".split(maxsplit=2)  # ['lo', 'ly', 'ly l']
"lo ly ly l".rsplit(maxsplit=2) # ['lo ly', 'ly', 'l']
"love\nlyy".splitlines()        # ['love', 'lyy']
# 删除前后缀
"love lyy".removeprefix('l')    # 'ove lyy'
"love lyy".removeprefix('y')    # 'love lyy'
"love lyy".removesuffix('y')    # 'love ly'
# 替换
"love lyy".replace('l', '0')    # '0ove 0yy'
"love lyy".replace('l', '0', 1) # '0ove lyy'

# 4. 特殊方法
# 字符串反转
"apple love"[::-1]      # 'evol elppa'
# 连接列表字符串
names = ['lyy', 'lly', 'gx']
' '.join(names)                 # 'lyy lly gx'
','.join(names)                 # 'lyy,lly,gx'
# 加密
# 生成密码本
source = "abcdefghig"
output = "0123456789"
password_table = str.maketrans(source, output)  # {97: 48, 98: 49, 99: 50, 100: 51, 101: 52, 102: 53, 103: 57, 104: 55, 105: 56}
# 加密
"apple love".translate(password_table)          # '0ppl4 lov4'
# 解密本
pass1 = str.maketrans(output, source)
# 解密
"0ppl4 lov4".translate(pass1)                   # 'apple love'

import string
string.digits           # '0123456789'
string.ascii_letters    # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.printable        # '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'

# 额外用法
# 如果没有输入就跳出
while True:
    msg = input(">:").strip()
    if not msg:break    # if len(msg) == 0:break