import itertools
a = list(itertools.permutations('МИМИКРИЯ'))
a = set(a)
c = 0
for x in a:
    b = ''.join(x)
    print(b)
    c +=1
print(c)