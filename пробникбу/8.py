from itertools import product
a = list(product('АНЯ', repeat=5))
c = 0
for x in a:
    b = ''.join(x)
    c += 1
    if b == 'НАААА':
        print(c)