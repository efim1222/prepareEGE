for x in range(312614, 312652):
    delit = []
    for y in range(1, x + 1):
        if x % y == 0:
            delit.append(y)
    if len(delit) == 6:
        print(x, delit)