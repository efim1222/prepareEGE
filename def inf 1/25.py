for x in range(2422000, 2422081):
    c = 0
    for y in range(1, x + 1):
        if x % y == 0:
            c += 1
    if c == 2:
        print(x)