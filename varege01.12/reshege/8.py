from itertools import * 
a = list(product('РУЧКА', repeat=3))
c = 0
for x in a:
    b = ''.join(x)
    if b.count('К') == 1:
        c += 1 
print(c)
    