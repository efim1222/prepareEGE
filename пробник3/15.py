for A in range(1, 1000):
    flag = 1
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ( ( (2 * x + 3 * y) < A) or (x > y) or (y > 24)) == 0:
                flag = 0
                break
    if flag == 1:
        print(A)