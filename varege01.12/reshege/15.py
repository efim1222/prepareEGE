for A in range(1, 1000):
    flag = 1
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ( ((x + 2 * y) < A) or (y > x) or (x > 20) ) == 0:
                flag = 0
                break
    if flag == 1:
        print(A)