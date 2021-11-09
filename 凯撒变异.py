s = 'afZ_r9VYfScOeO_UL^RWUc'
k = 'flag{'
res = ''
for i in range(len(s)):
    res += chr(ord(s[i])+(ord(k[0])-ord(s[0])+i))

print(res)