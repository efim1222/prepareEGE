with open('17 (1).txt') as a:
    s = [int(x) for x in a]
    res = []
    c = 0
    mx = 0
    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            if (s[i] + s[j]) % 8 == 0:
                c += 1
                mx = max(mx, s[i] + s[j])
            
print()