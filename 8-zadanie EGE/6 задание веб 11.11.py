import itertools
a = list(itertools.product('012345678', repeat=7))
c = 0
for x in a:
    b = ''.join(x)
    if b[0] != '0' and b[-1] != '3' and b[-1] != '4' and b[-1] != '7' and (not '000' in b)\
        and (not '111' in b) and (not '222' in b)and (not '333' in b)and (not '444' in b)and (not '555' in b)\
            and (not '666' in b) and (not '777' in b) and (not '888' in b):
                c += 1
print(c)                 
                            