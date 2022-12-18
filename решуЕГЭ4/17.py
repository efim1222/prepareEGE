f = open('17.txt')
s = [int(x) for x in f]
mx = c = 0
for i in range(len(s) - 1):
    for j in range(i + 1, len(s)):
        if (s[i] - s[j]) % 80 == 0:
            c += 1
            mx = max(mx, s[i] - s[j])
            
print(c, mx)