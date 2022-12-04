with open('17.txt') as a:
    s = [int(x) for x in a]
    c = 0
    mx = 0
    for x in range(len(s)-1):
        for j in range(x + 1, len(s)):
            if (s[x] - s[j]) % 2 == 0 \
                and (s[x] % 17 == 0 or s[j] % 17 == 0):
                    c += 1
                    mx = max(s[x] + s[j], mx)
                    print(mx)
    print(c)
    print(mx)