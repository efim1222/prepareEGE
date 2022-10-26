print('x y z w')
for x in range(0,2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if ((not x) and y or z and (not y) or (not z) and w) == False:
                    print(x, y, z, w)