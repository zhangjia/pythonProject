import hashlib

print(hashlib.sha256(b"hello").hexdigest())
print(hashlib.md5(b"hello").hexdigest())
print(hashlib.sha1(b"hello").hexdigest())