with open('17(3).txt') as a:
    s = [int(x) for x in a]
    c = mx = 0
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if (s[i] - s[j]) % 2 == 0 and \
                (s[i] % 19 == 0 or s[j] % 19 == 0):
                    c += 1
                    mx = max(mx, s[i] + s[j])
print(c, mx)