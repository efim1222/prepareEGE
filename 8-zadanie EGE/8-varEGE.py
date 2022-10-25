import itertools
a = list(itertools.product('АМРТ', repeat=4))
for x in a:
    b = ''.join(x)
    if b[0] != b[1] and b[1] != b[2] and b[2] != b[3] and b[0] != b[2] and b[0] != b[3] and b[1] != b[3] and b[2] != b[3]:
        print(b)
c = int('123', 4)
print(c+1)

