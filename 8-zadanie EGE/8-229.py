import itertools
a = list(itertools.product('0123456', repeat=7))
c = 0
for x in a:
    b = ''.join(x)
    if b[0] != '0' and b[0] != '3' and b[0] != '5':
        if '22' not in b or '44' not in b:
            c+=1
            print(b)
print(c)
