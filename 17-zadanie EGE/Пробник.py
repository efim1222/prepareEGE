with open('17.txt') as a:
    s = [int(x) for x in a]
    res = []
    cnt = 0
    for i in range(len(s)-1):
        if (s[i] + s[i+1]) % 2 != 0 and (s[i] * s[i+1]) % 3 == 0:
                res.append(s[i]+s[i+1])
                cnt +=1
    print(cnt, max(res))


