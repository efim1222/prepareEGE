import itertools as it
a = list(it.product('КОТ', repeat=6))
c = 0
for x in a:
    b = ''.join(x)
    if b.count('К') == 1:
        c += 1
print(c)