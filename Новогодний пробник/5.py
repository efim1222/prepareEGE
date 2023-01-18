def F(n):
    n2 = bin(n)[2:]
    n2rev = n2[::-1]
    n10end = int(n2rev, 2)
    return n10end

for x in range(101):
    if F(x) == 11:
        print(x)