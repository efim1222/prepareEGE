B = [1, 4, 5, 8, 10, 12, 13, 17, 18, 20]
C = [2, 6, 9, 12, 13, 18, 21, 24, 28, 33]
A = []
for x in range(1, 1000):
    if ( (x in C) or ((x in B) <= (x in A))) == False:
        A.append(x)
print(len(A))