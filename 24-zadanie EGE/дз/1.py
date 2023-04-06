with open('D:/GitHub/prepareEGE/24-zadanie EGE/24_4602.txt') as f:
    s = f.readline()
s = s.replace('BA', '*')
s = s.replace('BO', '*')
s = s.replace('CA', '*')
s = s.replace('CO', '*')
s = s.replace('DA', '*')
s = s.replace('DO', '*')
t = tmax = 0
for x in range(len(s)):
    if s[x] == '*':
        t += 1
        tmax = max(t, tmax)
    else:
        t = 0
print(tmax )
