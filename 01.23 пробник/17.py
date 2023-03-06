with open('17_2491.txt') as f:
    a = [int(x) for x in f]
c = 0
mx = -2324324324324234234234
sr = sum(a) / len(a)
for i in range(len(a) - 2):
    if (a[i] < sr or a[i+1] < sr or a[i+2] < sr) \
        and ('9' in str(a[i]) and '9' in str(a[i + 1]) \
            and '9' in str(a[i + 2])):
            c += 1
            mx = max(mx, a[i] + a[i + 1] + a[i + 2])
print(c, mx)