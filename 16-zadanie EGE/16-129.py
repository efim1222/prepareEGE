c = 0
def F(n):
    if n < 2:
        return n
    if n >= 2 and n % 2 == 0:
        return F(n/2) + 1
    if n >= 2 and n % 2 != 0:
        return F(3*n+1) + 1
for n in range(1,100001):
    if F(n) == 16:
        c+=1
        print(n)
print(c)