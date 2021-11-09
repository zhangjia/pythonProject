import re

def asciiTransform(str):
    str = str.split("/")
    print(str)
    res = ""
    for i in range(1,len(str)):
        res += chr(int(str[i]))
    return res


print(asciiTransform("/119/101/108/99/111/109/101/116/111/97/116/116/97/99/107/97/110/100/100/101/102/101/110/99/101/119/111/114/108/100"))