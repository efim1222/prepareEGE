def R(n):
    n2 = bin(n)[2:]
    if n2.count('1') % 2 == 0:
        n2 = '1' + n2
        n2 = n2 + '00'
    else:
        n2 += '11'
    return int(n2,2)
for n in range(1,10000):
    if R(n) >= 412:
        print(n)