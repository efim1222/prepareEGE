for a in range(1, 1000):
    f = 1
    for x in range(1, 1000):
        if (  ( (x % 2 == 0) <= (not(x % 3 == 0)) ) or (x + a >= 100) ) == 0:
            f = 0
            break
    if f == 1:
        print(a)