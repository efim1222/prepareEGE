from itertools import permutations
a = list(permutations('АТТЕСТАТ', r=8))
a = set(a)
c = 0
for x in a:
    b = ''.join(x)
    c += 1
    print(b, c)


