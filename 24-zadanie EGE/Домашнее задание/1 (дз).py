with open('1-2__z0t.txt') as a:
    s = [str(x) for x in a]
    lengths = []
    lengths2 = []
    z = ''
    string_of_min_F = ''
    for i in s:
        lengths.append(i.count('F')) 
        z = min(lengths)
        if i.count('F') == 16:
            string_of_min_F = i
    for aplh in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if aplh in string_of_min_F:
            lengths2.append(aplh + str(string_of_min_F.count(aplh)))
    print(lengths2)
    print("Ответ: Х" )