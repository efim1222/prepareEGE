def R(n):
    n2 = str(bin(n)[2:])
    c = []
    for x in n2:
        c.append(int(x))
    summa = sum(c)
    if n2[-1] == '0':
        n2 = n2 + str(bin(summa)[2:])
    else:
        n2 = '1' + n2 + '00'
    return int(n2, 2)
for n in range(1,10000):
    if R(n) < 1000:
        print(n)


