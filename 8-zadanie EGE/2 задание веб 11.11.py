import itertools
a = list(itertools.product('БАЛКОН', repeat=5))
c = 0
for x in a:
    b = ''.join(x)
    if b.count('Б') >= 1:
        c += 1
print(c)