v8 = ':\"AL_RT^L*.?+6/46'
v7 = 'harambe' # ebmarah
v6 = 7
tmp = ''
for i in range(len(v8)):
    c = ord(v7[i % v6]) ^ ord(v8[i])
    tmp += chr(c)

print(tmp)