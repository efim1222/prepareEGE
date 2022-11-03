with open('3__z0u.txt') as a:
    s = [str(x) for x in a]
    b = ''.join(s)
    c = 0
    p = 'P'
    while p in b:
        c +=1
    print(c)
    