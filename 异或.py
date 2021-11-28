

def getRes(a,b):
    l = range(10)
    res = ""
    for i in range(0, len(a), 2):
        res += chr((int('0x' + a[i] + a[i + 1], 16)) ^ b)
    return res

def getResByDoc(key,word):
    res = ""
    key = open(key,'rb').read()
    word = open(word,'rb').read()
    for i in range(len(key)):
        res += chr(key[i] ^ word[i])
    return res


ad1 = 'F:\\Google\\CTF\\b8c1caee-43d6-42ee-aecc-d72502a5ade2\\1.txt'
ad2 = 'F:\\Google\\CTF\\b8c1caee-43d6-42ee-aecc-d72502a5ade2\\2.txt'
print(getResByDoc(ad1,ad2))