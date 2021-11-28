import hashlib

filename = '/fllllllllllllag'
cookie_secret = '691711cd-02de-4940-bc64-8a908c50bcb8'
m = hashlib.md5()
m.update(filename.encode("utf-8"))
n = m.hexdigest()

v = cookie_secret + n
m = hashlib.md5()
m.update(v.encode("utf-8"))
n = m.hexdigest()
print(n)
