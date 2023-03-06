print('a b c d')
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            for d in 0, 1:
                if ( (a <= b) and (c <= d) or (not(c)) ) == 0:
                    print(a, b, c, d)