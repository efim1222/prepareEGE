with open('17 (2).txt') as a:
    s = [int(x) for x in a]
    c = mx = 0
    for x in range(len(s) - 1):
        for y in range(x + 1, len(s)):
            if (s[x] + s[y]) % 120 == 0:
                c += 1
                mx = max(mx, s[y] + s[x])
print(c, mx)