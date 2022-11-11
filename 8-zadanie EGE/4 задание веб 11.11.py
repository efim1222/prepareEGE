# Количество каждой буквы > 2
a = 'КОМБАЙН'
a1 = 'КОМБАН'
c = 0
for i in a1:
    for j in a:
        for k in a:
            for l in a:
                for m in a:
                    for n in a:
                        for o in a:
                            s = i+j+k+l+m+n+o
                            t = [x for x in a if s.count(x) > 2]
                            if (not 'АЙ' in s) and (not t):
                                c += 1
                                print(s)