for n in range(100000):
    s = '1' + n * '0'
    while '10' in s or '1' in s:
        if '10' in s:
            s = s.replace('10', '001', 1)
        else:
            if '1' in s:
                s = s.replace('1', '0', 1)
    print(n, len(s))