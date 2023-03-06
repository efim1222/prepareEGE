for x in '0123456789ABCDEFG':
    t1 = int('10' + x + '0', 17) + int('F0' + x + 'FF', 17)
    if t1 % 13 == 0:
        print(x, t1 // 13)
