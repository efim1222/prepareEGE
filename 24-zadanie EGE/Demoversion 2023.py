# Текстовый файл состоит из символов
# A, C, D, F
# и O.
# Определите максимальное количество идущих подряд пар символов вида
# согласная + гласная
# в прилагаемом файле.
# Для выполнения этого задания следует написать программу
with open('24.txt') as a:
    b = list(str(x) for x in a)
    s = ''.join(b)
    # ca da fa co do fo
    s = s.replace('CA', '*')
    s = s.replace('DA', '*')
    s = s.replace('FA', '*')
    s = s.replace('CO', '*')
    s = s.replace('DO', '*')
    s = s.replace('FO', '*')
    count = countMAX = 0
    for i in range(len(s)):
        if s[i] == '*':
            count += 1
            countMAX = max(count, countMAX)
        else:
            count = 0
    print(countMAX)

