from itertools import *
a = list(product('01234567', repeat=5))
c = 0
for x in a:
    b = ''.join(x)
    if b[0] != '0':
        if b.count('4') == 2:
            if '14' not in b and '41' not in b and '34' not in b and \
                '43' not in b and '54' not in b and '45' not in b and \
                    '74' not in b and '47' not in b:
                        c += 1
print(c)
        