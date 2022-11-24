with open('24 (1).txt') as a:
    s = [x for x in a]
    alph = 'ABCDEFGHIJKLMNOPQRSTUBWXYZ'
    for x in range(len(s)):
        s[x] = s[x].replace('\n', '')
    kolvoG=[]
    for x in s:
        kolvoG.append(x.count('G'))
    mn = min(kolvoG)
    ind = kolvoG.index(min(kolvoG))
    sn = s[ind]
    for k in alph:
        if k in sn:
            print(k, sn.count(k))
        

