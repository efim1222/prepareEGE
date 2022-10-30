n = int(input())
m = int(input())
c = 0
for a in range(1, 1000):
    for d in range(1, 1000):
        if a + (n-1) * d <= m:
            c += 1
print(c)