print('a b c d')
for a in range(0,2):
    for b in range(0, 2):
        for c in range(0, 2):
            for d in range(0, 2):
                if ((a <= b) and (c <= d) or (not c)) == False:
                    print(a, b, c, d)