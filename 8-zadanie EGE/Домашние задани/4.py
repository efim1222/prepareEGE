import itertools as it
a = list(it.permutations('01234567', r=5))
c = 0
forbiddens = list(it.permutations('1357', r=2)) + list(it.permutations('0246', r=2))
for x in a:
    b = ''.join(x)
    if b[0] != '0':
        for forbidden in forbiddens:
            s = ''.join(forbidden)
            if s in b:
                break
        else:
            c += 1
            

print(c)            
               