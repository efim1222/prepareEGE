f = open('D:/GitHub/prepareEGE/апробация/26_8512.txt')
k = int(f.readline())
n = int(f.readline())
time = []
for s in f:
    time.append([int(x) for x in s.split()])
time.sort()

boxes = [-1] * k
c = 0
last_start = - 1
last_nomer = -1

for pas in time:
    start = pas[0]
    end = pas[1]
    
    for i in range(k):
        if boxes[i] <= start:
            boxes[i] = end + 1
            c += 1
            if start > last_start:
                last_start = start
                last_nomer = i + 1
            break
            
print(c, last_nomer)