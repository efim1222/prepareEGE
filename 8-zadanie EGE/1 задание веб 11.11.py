import itertools
a = list(itertools.product('ABCX', repeat=5))
c = 0

for x in a:
    b = ''.join(x)
    if b[-1] == 'X' or 'X' not in b:
        print(b)
        c += 1
print(c)