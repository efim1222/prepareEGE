def f(n):
    n2 = bin(2*n)[2:]
    n2 = n2 + str(n2.count('1') % 2)
    n2 = n2 + str(n2.count('1') % 2)
    return int(n2,2)
# for n in range(1000):
    # if f(n) > 249:
        # print(n)
print(f(31))