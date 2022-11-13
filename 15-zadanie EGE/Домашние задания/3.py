for A in range(1000):
    flag = 1
    for x in range(1000):
        for y in range(1000):
            if ( (x > A) or (y < A) or (2*x + y != 48) ) == False:
                flag = 0
                break
    if flag == 1:
        print(A)