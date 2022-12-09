from itertools import *

c = 0
a = list(product('РУСЛАН', repeat=5))
for x in a:
    b = ''.join(x)
    if b.count('У') <= 1 and b.count('А') <= 1:
        c += 1
print(c)
    