a = 23100
base = 4
a1 = ''
while a > 0:
    a1 = str(a % base) + a1
    a //= base
print(a1)