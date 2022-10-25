P = list(range(117, 158))
Q = list(range(129, 181))
A = []
for x in range(1,1000):
    if ( (x in P) <= (((x in Q) and (not(x in A))) <= (not(x in P)))) == False:
        A.append(x)
print(A)
print(len(A))