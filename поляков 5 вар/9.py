with open('9 (2).txt') as f:
    c = 0
    for s in f:
        a = sorted(int(x) for x in s.split())
        if len(a) - len(set(a)) >= 1:
            for n in a:
                if a.count(n) == 2
        