# 凯撒密码遍历
def casearDecrypt(ciphertext, source_char, destination_char, list_all):
    if list_all == True:
        for offset in range(1, 27):
            convertChar(offset)
    else:
        offset = ord(destination_char) - ord(source_char)
        convertChar(offset,-1)


def convertChar(offset):
    chars = "abcdefghijklmnopqrstuvwxyz"
    for char in ciphertext:
        is_upper_flag = 0
        if char.isupper():
            char = char.lower()
            is_upper_flag = 1

        if char not in chars:
            outputChar(is_upper_flag, char)
            continue

        tempchar_ascii = ord(char) + offset
        tempchar = chr(tempchar_ascii)
        if tempchar not in chars:
            if offset < 0:
                tempchar_ascii += len(chars)
            else:
                tempchar_ascii -= len(chars)
        tempchar = chr(tempchar_ascii)
        outputChar(is_upper_flag, tempchar)

    print("：",offset)


def outputChar(is_upper_flag, char):
    if is_upper_flag == 1:
        print(char.upper(), end="")
    else:
        print(char, end="")


ciphertext = input("请输入凯撒密码:\n")
while True:
    operation = input("List all results?y/n:")
    if operation == 'y' or operation == 'Y':
        casearDecrypt(ciphertext, '', '', True)
        break
    elif operation == 'n' or operation == 'N':
        des_char = input("Please input destination_char:\n")
        sors_char = input("Please input source_char:\n")
        casearDecrypt(ciphertext, sors_char, des_char, False)
        break
    else:
        print("Input error! Please input y/n:")

