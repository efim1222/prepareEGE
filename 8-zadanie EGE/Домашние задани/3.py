import itertools
a = list(itertools.product('ТИМОФЕЙ', repeat=5))

c = 0
for x in a:
    b = ''.join(x)
    if b.count('Т') >= 1 and b.count('Й') <= 1:
        c += 1
print(c)