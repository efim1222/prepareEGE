from itertools import *
a = list(product('0123456', repeat=5))
c = 0
for x in a:
    b = ''.join(x)
    if b[0] != '0':
        if b.count('5') == 1 and \
            '25' not in b and '52' not in b and '45' not in b and '54' not in b and\
                '65' not in b and '56' not in b and '05' not in b and '50' not in b:
                    c += 1
print(c)