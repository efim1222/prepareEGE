for a in range(1, 1001):
    flag = 0
    for x in range(1, 1001):
        for y in range(1, 1001):
            if (( y - 40 < a) and ( 30 - y < a) or (x * y > 20)) == False:
                flag = 1
                break
    if flag == 0:
        print(a)