import hashlib


m = hashlib.md5()
m.update("abc123".encode())
a = m.hexdigest()




print(a)
