import itertools
a = list(itertools.permutations('КОМБАЙН', r=7))
c = 0
for x in a:
    b = ''.join(x)
    if b[0] != 'Й':
        if not "АЙ" in b:
            c += 1
print(c)
    