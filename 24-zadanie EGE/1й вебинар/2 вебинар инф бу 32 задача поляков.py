# В текстовом файле k7b-6.txt находится цепочка из символов латинского алфавита A, B, C, D, E, F.
# Найдите максимальную длину цепочки вида DAFDAFDAF.... (состоящей из фрагментов DAF, последний фрагмент может быть неполным).

with open('k7b-6.txt') as a:
    s = list(str(x) for x in a)
    b = ''.join(s)
    b1 = 'D'
    while b1 in b:
        if b1[-1] == 'D':
            b1 += 'A'
        elif b1[-1] == 'A':
            b1 += 'F'
        else:
            b1 += 'D'
    print(len(b1) - 1)

