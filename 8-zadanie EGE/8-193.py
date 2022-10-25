c = 0
alf = '01234'
alf1 = '3'
for x in alf1:
    for y in alf:
        for z in alf:
            for x1 in alf:
                for x2 in alf:
                    for x3 in alf:
                        w = x+y+z+x1+x2+x3
                        if int(w, 5) % 2 == 0:
                            print(w)
                            c +=1
print(c)