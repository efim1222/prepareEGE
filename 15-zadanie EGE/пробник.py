P = list(range(10, 41))
Q = list(range(5, 16))
R = list(range(35, 51))
A = []
for x in range(1,1000):
    if ( ((x in A) or (x in P))   or   ((x in Q) <= (x in R))) == False:
        A.append(x)
print(A)
print(len(A))