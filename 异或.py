s = 'EEE4E9EFF3F0E7DAD7E1BDD7E1E6FEEDFAFCE1EAE4EDF5'
l = range(10)
res = ""
for i in range(0,len(s),2):
    res += chr((int('0x'+s[i]+s[i+1],16)) ^ 0x88)

print(res)