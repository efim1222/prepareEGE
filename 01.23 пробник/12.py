for n in range(3, 51):
    s = '>' + n * '1' + n * '2' + n * '3'
    while '>1' in s or '>2' in s or '>3' in s:
        if '>1' in s:
            s = s.replace('>1', '22>3', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>3' in s:
            s = s.replace('>3', '11>2', 1)
    if sum(int(x) for x in s if x != '>') % 7 == 0:
        print(n)
    