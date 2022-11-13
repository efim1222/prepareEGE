import itertools
a = list(itertools.product('01234567', repeat=5))
c = 0
for x in a:
    b = ''.join(x)
    if b[0] != '0' and b.count('6') == 1 and ('16' not in b) and ('61' not in b)\
        and ('36' not in b) and ('63' not in b) and ('56' not in b) and ('65' not in b)\
            and ('76' not in b) and ('67' not in b):
                c += 1
print(c)