import string
import binascii
import itertools

# 可打印字符
printable = string.printable
crc32 = 0x6526B899 #对应文件里的crcc32信息
sign = 1
for i in itertools.product(printable, repeat=4): # repeat对应密码长度
    s = ''.join(i)
    if crc32 == (binascii.crc32(s.encode()) & 0xffffffff):
        print(s)
        sign = 0
    # 退出循环
    if sign == 0:
        break