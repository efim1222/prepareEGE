space = ' '
for x in range(1,11):
    for y in range(1,11):
        space = ' '*(1-((x*y) // 10))
        print( x*y, sep=' ', end=' ')
    print()