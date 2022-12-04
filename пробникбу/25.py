mx = 0
for x in range(567123, 569322):
    delit = []
    for y in range(1, x + 1):
        if x % y == 0:
            delit.append(y)
    mx = max(len(delit), mx)
    print(mx, x)