with open('24_3228.txt') as f:
    s = f.readline()
s = s.replace('AC', '*')
ac = 0
acmax = 0

for x in range(len(s)):
    if s[x] == '*':
        ac += 1
        acmax = max(acmax, ac)
    else:
        ac = 0

s = s.replace('AB', '#')
ab = 0
abmax = 0

for x in range(len(s)):
    if s[x] == '#':
        ab += 1
        abmax = max(abmax, ab)
    else:
        ab = 0

g = 0 
gmax = 0 
for x in range(len(s)):
    if s[x] == '*' or s[x] == '#':
        g += 1
        gmax = max(gmax, g)
    else:
        g = 0
print(gmax)