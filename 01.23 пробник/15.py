b = list(range(50, 71))
for a in range(1, 1000):
    f = 1
    for x in range(1, 1000):
        if ((x % a == 0) or ((x % 23 == 0) <= (not(x in b)))) == 0:
            f = 0
            break
    if f == 1:
        print(a)