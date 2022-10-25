def DEL(n,m):
    if n % m == 0:
        return True
    else: return False
for A in range(1,1000):
    k = 0
    for x in range(1,1000):
        if (((DEL(x,2)) <= (not(DEL(x,3)))) or (x+A>=80)):
            k +=1
    if k == 999:
        print(A)
