print('x y z w F')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                print(x, y, z, w, bool(x and (y <= z) and ((not y) <= ((not z) == w))))