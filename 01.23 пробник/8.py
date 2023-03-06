a = 'РУСЛАН'
c = 0
for i in a:
    for j in a:
        for k in a:
            for l in a:
                for m in a:
                    s = i + j + k + l + m
                    if (s.count('У') <=1 and s.count('А') <= 1):
                        c += 1 