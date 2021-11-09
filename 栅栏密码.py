
def encode(string, key):#需要加密的字符串以及加密栏数
    i = 0
    enlist = []
    for j in range(0, key):
        enlist.append('')#添加分组，列表的一个元素相当于一个分组

    while i < len(string):#分组重排进行加密
        for k in range(0, key):
            if i >= len(string):
                break
            enlist[k] += string[i]
            i += 1
        for k in range(1, key-1):
            if i >= len(string):
                break
            enlist[key-1-k] += string[i]
            i += 1
        enstr = ''
    for i in range(key):
       	enstr += enlist[i]
    return enstr


def decode(string, key):  # 解密字符串以及解密栏数
   try:
       de_key = 2 * key - 2  # 一个部分的长度
       length = len(string) // de_key  # 确定有多少个完整部分
       r = len(string) % de_key  # 最后不完整部分的长度
       delist = []
       for i in range(key):
           delist.append('')  # 重新排布分组
       # 确定第一个分组
       if r == 0:
           delist[0] += string[0:length]
           s = length
       else:
           delist[0] += string[0:length + 1]
           s = length + 1
       # 确定第二个到第key-1个分组
       for i in range(1, key - 1):
           l = length * 2  # 这几个分组长度至少是完整部分数量的两倍
           # 最后一个不完整部分对应当前分组有几个元素
           if r > i:
               l += 1
           if r > de_key - i:
               l += 1

           delist[i] += string[s:s + l]
           s = s + l
       # 确定最后一个分组
       delist[key - 1] += string[s:]
       # 排布分组确定原文字符串
       destr = ''
       j = 0
       for i in range(0, len(string)):
           destr += delist[j][0]
           delist[j] = delist[j][1:]
           if j == key - 1:
               flag = 0
           if j == 0:
               flag = 1
           if flag:
               j += 1
           else:
               j -= 1
       return destr
   except:
       print(key,"不正确")
s = 'SUNYHAGU'
for i in range(len(s)):
    res = decode(s, i)
    # res = encode(s, i)
    if res != None and 'flag' in res :
        print(res + "是正确的")
    else:
        print(res)