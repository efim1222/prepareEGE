def F(n):
    if len(str(n)) == 3:    
        n1 = int(str(n)[0]) + int(str(n)[1])
        n2 = int(str(n)[1]) + int(str(n)[2])
        return str(max(n1, n2)) + str(min(n1, n2))
    else: return 0
for n in range(100, 1000):
    if F(n) == '1412':
        print(n)