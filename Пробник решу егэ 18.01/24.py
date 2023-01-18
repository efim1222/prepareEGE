f = open("24_demo.txt")
s = f.read()
t = 0
for x in range(len(s) - 2):
    if s[x] == 'X' and s[x + 1] == 'Y' and s[x + 2] == 'Z':
        t += 1
print(t)