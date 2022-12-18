from itertools import *
c = 0
a = list(permutations('ОЛЬГА', r=5))
for x in a:
    b = ''.join(x)
    if b[0] != 'Ь' and b.count('ОЬ') == 0 and b.count('АЬ') == 0:
        c += 1