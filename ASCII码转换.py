import re

def asciiTransform(str):
    str = str.split("/")
    res = ""
    for i in range(1,len(str)):
        res += chr(int(str[i]))
    return res

def strTransformAscII(s):
    res = ""
    for i in s:
       res += str(ord(i)) + ","
    return res
def strTransformPHP(s):
    res = ""
    for i in s:
        res += ('chr('+str(ord(i))+')'+'.')
    return res[:-1]
print(asciiTransform("/119/101/108/99/111/109/101/116/111/97/116/116/97/99/107/97/110/100/100/101/102/101/110/99/101/119/111/114/108/100"))
print(strTransformAscII("$_POST['jia']"))
print(strTransformPHP("12"))