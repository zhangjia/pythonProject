string = "35352c35362c35342c37392c3131352c36392c3131342c3131362c3130372c34392c3530"
flag = ''
for i in range(0,len(string), 2):
    s = "0x" + string[i] + string[i + 1]
    flag += chr(int(s, 16))
print(flag)
print(ord('f'))