with open('1-2__z0t.txt') as a:
    s = [str(x) for x in a]
    lengths = []
    lengths2 = []
    minb = ''
    stroka = ''
    for i in s:
        lengths.append(i.count('B'))
        minb = min(lengths)
        if i.count('B') == 20:
            stroka = i
    for alph in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if alph in stroka:
            print(alph, stroka.count(alph))
        if alph in stroka:
            lengths2.append(stroka.count(alph))
    print('Ответ: Е', ' встречается в строке, содержащий минимальное количество букв В,', max(lengths2), ' раз') 