import itertools
a = list(itertools.product('ОНИКС', repeat=6))
c = 0
for x in a:
    b = ''.join(x)
    if b.count('С') == 3 and b.count('О') == 1:
        print(b)
        c += 1
print(c)