for x in range(200, 1000):
    s = x * '1'
    while '111' in s or '222' in s:
        s = s.replace('111', '22', 1)
        s = s.replace('222', '1', 1)
    if '2' not in s:
        print(x, s)