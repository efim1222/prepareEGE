for x in range(1,56475):
    count = 0
    for y in range (2, x):
        if x%y==0:
            count+=1
    if count == 0:
        print(x)
