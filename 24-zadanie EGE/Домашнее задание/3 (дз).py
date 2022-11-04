with open('3__z0u.txt') as a:
    s = [str(x) for x in a]
    b = ''.join(s)
    l = lmax = 1
    for i in range(len(b)):
        if b[i] != 'P':
            l += 1
            lmax = max(l, lmax)
        else:
            l = 1
    print(lmax)
    