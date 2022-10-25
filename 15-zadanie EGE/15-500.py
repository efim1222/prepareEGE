def Del(n,m):
    return n % m ==0

for A in range(1,1000):
    A_podoshel = True
    for x in range(1,1000):
        if ((Del(x,7) <= (not(Del(x,21)))) or (2*x + A>=120)) == False:
            A_podoshel = False
            break
    else:
        print(A)
