import hashlib

s = 'TASC'
s2 ='O3RJMV'
s3 = 'WDJKX'
s4 = 'ZM'
res = ""
for x in range(65,91):
    for y in range(65, 91):
        for z in range(65, 91):
            res = s + chr(x) +s2 + chr(y) + s3 +chr(z) + s4
            print(hashlib.md5(res.encode(encoding='utf-8')).hexdigest())
