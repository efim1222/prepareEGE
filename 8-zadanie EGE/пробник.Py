a = 349
base = 4
a4 = ''
while a>0:
    a4 = str(a % base) + a4
    a //= base
print(a4)