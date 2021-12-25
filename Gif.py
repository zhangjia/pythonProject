# 图片二进制识别
from PIL import Image

result = ""
for num,i in enumerate(range(104)): #把range生成的list按照键值对分给num 和i
    img = Image.open(f"/Users/zhangjia/Downloads/gif/{i}.jpg")
    im = img.convert("RGB")
    r,g,b = im.getpixel((1,1)) #返回坐标点（1，1）处的red，green，blue的数值
    if r != 255:
        result += "1"
    else:
        result += "0"


for i in range(0,len(result),8):
    byte = result[i:i+8]
    print(byte)
    # print(int(byte, 2))
    # print(chr(int(byte, 2/)), end="")