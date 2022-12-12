def f(n):
    n2 = bin(n)[2:]
    summa = sum([int(x) for x in n2])
    if summa % 2 == 0:
        n2 = n2[1:]
    else:
        n2 = '1' + n2 + '00'
    n2ot = int(n2, 2)
    n22 = bin(n2ot)[2:]
    summa1 = sum([int(x) for x in n22])
    if summa1 % 2 == 0:
        n22 = n22[1:]
    else:
        n22 = '1' + n22 + '00'
    nres = int(n22, 2)
    return nres
    
for n in range(1, 100):
    if f(n) > 100:
        print(n)
