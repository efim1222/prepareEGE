
for x in range(125256, 125331):
    cnt = 0
    delit = []
    for i in range(1, x+1):
        if x % i == 0 and i % 2 == 0:
            cnt += 1
            delit.append(i)       
    if cnt == 6:
        print(sorted(delit))