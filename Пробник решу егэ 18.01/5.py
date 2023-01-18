def F(n):
    n2 = bin(n)[2:]
    n2sum = sum(int(x) for x in n2)
    n2 = n2 + str(n2sum % 2)
    n2sum2 = sum(int(x) for x in n2)
    n2 = n2 + str(n2sum2 % 2)
    return int(n2, 2)

for x in range(1, 1000):
    if F(x) > 396:
        print(x, F(x))   