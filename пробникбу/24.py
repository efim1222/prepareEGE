with open('24.txt') as a:
    a = [x for x in a]
    s = ''.join(a)
    s = s.replace('/n', '')
    s = s.replace('X', '*')
    t = ''
    while t in s:
        t += '*'
    print(len(t) - 1)