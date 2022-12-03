def f(N):
    N2 = bin(N)[2:]
    N2 = N2[1:]
    NDES = int(N2, 2)
    NRAS = N - NDES
    return NRAS

c = 0
a = set()
for x in range(10, 1000+1):
    a.add(f(x))
print(len(a))