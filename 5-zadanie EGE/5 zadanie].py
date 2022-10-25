print('x1x2x3x4x5x6')
for x1 in range(2):
    for x2 in range(2):
        for x3 in range(2):
            for x4 in range(2):
                for x5 in range(2):
                    for x6 in range(2):
                        if ((x2 and x4) or (x4 and x6) or (x6 and x2)) == 0:
                            print(x1, x2, x3, x4, x5, x6)