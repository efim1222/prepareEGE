def prost(x):
    c = 0
    for y in range(2, x):
        if x % y == 0:
            c += 1
    if c == 0:
        return 1
    else:
        return 0

for n in range(1, 1000):
    s = '>' + 23 * '1' + n * '2' + 25 * '3'
    while '>1' in s or '>2' in s or '>3' in s:
        if '>1' in s:
            s = s.replace('>1', '1>', 1)
        if '>2' in s:
            s = s.replace('>2', '>3', 1)
        if '>3' in s:
            s = s.replace('>3', '>11', 1)
    znsum = sum([int(x) for x in s if x != '>'])
    if prost(znsum) == 1:
        print(n, znsum)
        break
# 3