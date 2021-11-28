import hashlib

filename = '/fllllllllllllag'

m = hashlib.md5()  # 构建MD5对象
m.update(filename.encode("utf-8"))  #设置编码格式 并将字符串添加到MD5对象中
n = m.hexdigest() #  hexdigest()将加密字符串 生成十六进制数据字符串值
print("n = ",n)


cookie_secret = '60834def-5bfe-422d-bc92-bcd9e421a4a6'
v = cookie_secret + n

print("v = ",v)
m = hashlib.md5() #
m.update(v.encode("utf-8"))
res = m.hexdigest()
print(res)


# md5(cookie_secret+md5(/fllllllllllllag))