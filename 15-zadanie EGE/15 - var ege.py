def Del(n,m):
    return n % m ==0

for A in range(1,1000):
    A_podoshel = True
    for x in range(1,1000):
        if ((Del(x,3) <= (not(Del(x,5)))) or (x + A>=70)) == False:
            A_podoshel = False
            break
    if A_podoshel == True:
        print(A)
