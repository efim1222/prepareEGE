def F(n):
    n2 = bin(n)[2:]
    n2m = []
    for x in n2:
        n2m.append(int(x))
    n2s = sum(n2m)
    n2 = n2 + str(n2s % 2)
    
    n2m2 = []
    for y in n2:
        n2m2.append(int(y))
    n2s2 = sum(n2m2)
    n2 = n2 + str(n2s2 % 2)
    
    return int(n2, 2)


for n in range(1, 100):
    if F(n) > 199:
        print(n)
        break