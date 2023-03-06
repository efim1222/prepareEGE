from itertools import *
c = 0
a = list(product('0123456789', repeat=6))
def pd(n):
    digits = '0123456789AB'
    base = 12
    r = ''
    while n > 0: 
        r += digits[n % base]
        n //= base
    return int(r[::-1][0], 12)

for x in a:
    b = ''.join(x)
    if b[0] != '0':
        if int(b) % pd(int(b)) == 0:
            c += 1
print(c)
    