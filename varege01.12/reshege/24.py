with open('24(2).txt') as a:
    s = [x for x in a]
    b = ''.join(s)
    b = b.replace('/n', '')
    b = b.replace('XZZY', '*')
    b = b.split('*')
    a = list(map(len, b))
    print(max(a))