def f(n):
    n2 = bin(n)[2:]
    sm = sum(int(x) for x in n2)
    if sm % 2 == 0:
        n2 = n2[1:]
    else:
        n2 = '1' + n2 + '00'
    n2 = int(n2, 2)
    n2 = bin(n2)[2:]
    sm = sum(int(x) for x in n2)
    if sm % 2 == 0:
        n2 = n2[1:]
    else:
        n2 = '1' + n2 + '00'
    return int(n2,2)
for n in range(1, 1000):
    if f(n) > 100:
        print(n)
    

    