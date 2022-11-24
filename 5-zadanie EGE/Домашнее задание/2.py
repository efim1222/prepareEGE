def F(n):
    n2 = bin(n)[2:]
    n2m = []
    for x in n2:
        n2m.append(int(x))
    n2s = sum(n2m) % 2
    n2 = n2 + str(n2s) + str(n2s)
    return int(n2, 2)
    
for n in range(1000):
    if F(n) > 57:
        print(F(n))
        break