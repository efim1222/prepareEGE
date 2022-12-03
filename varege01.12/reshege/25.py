for x in range(10000000, 10100000):
    delit = []
    for y in range(1, int(x ** 0.5) + 1):
        delit.append(x // y)
    if delit[-2] + delit[-3] < 10000:
        print(x, delit)