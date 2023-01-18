P = list(range(69, 91))
Q = list(range(77, 114))
A = []
for x in range(1, 1000):
    if ( (x in Q) <= (((x in P) == (x in Q)) or ((not(x in P))  <= (x in A))) ) == 0:
        A.append(x)
print(A)
print(max(A) - min(A))