b = []
for n in range(41, 50):
    a = '>' + n * '0' + n * '1' + n * '2'
    while '>1' in a or '>2' in a or '>0' in a:
        if '>1' in a:
            a = a.replace('>1', '22>', 1)
        if '>2' in a:
            a = a.replace('>2', '00>', 1)
        if '>0' in a:
            a = a.replace('>0', '11>', 1)
    a = a.replace('>', '1', 1)
    print(a)
    su = sum(int(x) for x in a if x in '0123456789')
    print(su)
    if su % 100 == 77:
        print(n)
        break