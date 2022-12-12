f = open('24-224.txt')
s = f.readlines()
s = ''.join(s)
s = s.replace('BAC', '*')
s = s.replace('CAB', '*')
t = ''
while t in s:
    t += '*'
print((len(t) - 1) * 3)