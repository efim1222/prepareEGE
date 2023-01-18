alph = '0123456789ABCDEF'

for x in alph:
    s1 = '8' + x +'834'

    s2 = '44' + x + '27'
    
    s = int(s1, 16) + int(s2, 16) 
    if s % 23 == 0:
        print(s, s // 23, x)
    