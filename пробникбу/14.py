base = 7
a = 357
a7 = ''
while a > 0:
    a7 = str(a % base) + a7
    a //= base
print(a7)