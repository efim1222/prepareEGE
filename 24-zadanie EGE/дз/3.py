with open('24_6029.txt') as f:
    s = f.readline()
ml = 0
s = s.strip().split('D')
for i in s:
    cl = 1
    for j in range(1, len(i) - 1, 2):
        if i[j] + i[j + 1] == 'EF':
            cl += 2
        else:
            ml = max(cl, ml)
            cl = 1
    ml = max(cl, ml)
print(ml)