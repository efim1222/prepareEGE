with open('24.txt') as a:
    s = [str(x) for x in a]
    b = ''.join(s)
    cnt = 0
    mx = 1
    for i in range(len(b)-1):
        if b[i] == 'P' and b[i+1]=="P":
            cnt = 1
        else:
            cnt += 1
            mx = max(cnt, mx)
    print(mx)