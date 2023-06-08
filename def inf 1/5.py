def f(n):
    n2 = bin(n)[2:]
    if n2.count('1') % 2 == 0:
        n2 = '10' + n2[2:] + '1'
    else:
        n2 = '1' + n2[2:] + '11'
    return int(n2, 2)

for n in range(1000):
    if f(n) >= 100:
        print(n)
        break
print(f(40))