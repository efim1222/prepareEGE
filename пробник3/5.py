def f(N):
    nres = ''
    n = str(N)
    n1 = str(int(n[0]) * int(n[1]))
    n2 = str(int(n[2]) * int(n[3]))
    if int(n1) > int(n2):
        nres = n1 + n2
    else:
        nres = n2 + n1
    return nres


for n in range(1000, 10000):
    if f(n) == '124':
        print(n)
        break
    