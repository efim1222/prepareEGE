s = 729 ** 8 - 3 ** 18 + 85
base = 9
s9 = ''
while s > 0:
    s9 = str(s % base) + s9
    s //= base
print(s9.count('0'))