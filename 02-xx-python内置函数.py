shuru = input('''Let me repeat what you say!
Please input an number!''')
while True:
    print(shuru, end='')
# 这里运用了内置print函数与input函数
# 内置函数int()可以将数字字符串转化为字符
# 函数str()可以将数值转化为字符串
# int()妙用：
# zs = int(44.5434)直接取出整数
# 即 zs = 44
# 内置函数可以混用：如：str(int(input('输入个数字吧')))
