def od(n, m):
    ndel = []
    mdel = []
    odinak = []
    for i in range(2, n + 1):
        if n % i == 0:
            ndel.append(i)
    for x in range(2, m + 1):
        if m % x == 0:
            mdel.append(x)
    for j in ndel:
        for k in mdel:
            if j == k:
                odinak.append(j)
    if len(odinak) >= 1:
        return True
    else:
        return False

for A in range(1, 50):
    if all( ( (od(x, 42) <= (not od(x, 7))) or ((x + A)>=25)) for x in range(1, 1000)):
        print(A)