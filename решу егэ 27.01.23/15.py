for A in range(0, 1000):
    f = 1
    for x in range(0, 1000):
        for y in range(0, 1000):
            if (((x < 6) <= (x**2 < A)) and ((y**2 <= A) <= (y <= 6))) == 0:
                f = 0
                break
    if f == 1:
        print(A)
    