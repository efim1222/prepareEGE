def R(n):
    n1 = bin(n)[2:]
    if n1.count('1') % 2 ==0:
        n1 = '10' + n1[2:] + '0'
    else:
        n1 = '11' + n1[2:] + '1'
    return int(n1, 2)
for n in range(1, 100):
    if R(n) >= 16:
        print(n)