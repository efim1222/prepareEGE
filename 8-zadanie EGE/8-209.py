import itertools
a = list(itertools.permutations('АПЕЛЬСИН', r=7))
c = 0
for x in a:
    b = ''.join(x)
    if b[0] != 'Ь' and b[-1] != 'Ь':
        if 'ЕЬЕ' not in b and "АЬА" not in b and "ИЬИ" not in b:
            if 'ЬЕ' not in b and "ЬА" not in b and "ЬИ" not in b:
                if 'ЕЬ' not in b and "АЬ" not in b and "ИЬ" not in b:
                    print(b)
                    c +=1
print(c)