import itertools
a = list(itertools.product('ABCDXY', repeat=4))
c = 0
for x in a:
    b = ''.join(x)
    if (b[0] == 'X' or b[0] == 'Y') and b[1] != 'X' and b[2] != 'X' \
        and b[3] != 'X' and b[1] != 'Y' and b[2] != 'Y' and b[3] != 'Y':
        c += 1
print(c)