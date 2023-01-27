import itertools as it
a = list(it.product('КАТЕР', repeat=6))
c = 0
for x in a:
    b = ''.join(x)
    if b[0] == 'Р' and b[-1] == 'К':
        c += 1 
print(c)