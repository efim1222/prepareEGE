def M(N):
    delit = []
    for x in range(1, N):
        if N % x == 0:
            delit.append(x)
    if len(delit) >= 2:        
        return delit[-1] + delit[-2]
    if len(delit) < 2: return 0

for x in range(10_000_000, 10_000_0000):
    if 0 < M(x) < 10000:
        print(M(x)) 