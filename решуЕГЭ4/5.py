def f(n):
    n2 = bin(n)[2:]
    if len(n2) == 1:
        n2 = '0000000' + n2
    if len(n2) == 2:
        n2 = '000000' + n2
    if len(n2) == 3:
        n2 = '00000' + n2
    if len(n2) == 4:
        n2 = '0000' + n2
    if len(n2) == 5:
        n2 = '000' + n2
    if len(n2) == 6:
        n2 = '00' + n2
    if len(n2) == 7:
        n2 = '0' + n2
    n2m = [x for x in n2]
    if n2m[0] == '1':
        n2m[0] = '0'
    else:
        n2m[0] = '1'
        
    if n2m[1] == '1':
        n2m[1] = '0'
    else:
        n2m[1] = '1'
        
    if n2m[2] == '1':
        n2m[2] = '0'
    else:
        n2m[2] = '1'
        
    if n2m[3] == '1':
        n2m[3] = '0'
    else:
        n2m[3] = '1'
        
    if n2m[4] == '1':
        n2m[4] = '0'
    else:
        n2m[4] = '1'
        
    if n2m[5] == '1':
        n2m[5] = '0'
    else:
        n2m[5] = '1'
        
    if n2m[6] == '1':
        n2m[6] = '0'
    else:
        n2m[6] = '1'
        
    if n2m[7] == '1':
        n2m[7] = '0'
    else:
        n2m[7] = '1'
    n2 = ''.join(n2m)
    n2dec = int(n2, 2)
            
    return n2dec - n
    
    
print(f(71))
# 61