import itertools
a = list(itertools.permutations('МАРИНА', r=6))
a = set(a)
c = 0
for x in a:
    b = ''.join(x)
    if b[0] != 'А' and b[0] != 'И':
        print(b)
        c +=1
print(c)