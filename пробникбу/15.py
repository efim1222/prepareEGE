for A in range(1, 1000):
    flag = 1
    for x in range(1, 1000):
        for y in range(1, 1000):
            if (((abs(x - 1) + abs(y -3)) > 4) or ((x + y - 3) <= A)) == 0:
                flag = 0
                break
    if flag == 0:
        print(A)
            