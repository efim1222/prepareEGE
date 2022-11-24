P = list(range(8, 40))
Q = list(range(23, 59))
A = []
for x in range(1, 1000):
    if ( ((x in P) or (x in A)) <= ((x in Q) or (x in A))) == 0:
        A.append(x)
print(len(A))