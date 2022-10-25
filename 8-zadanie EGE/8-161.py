import itertools
a  = list(itertools.permutations('01234567', r=6))
count = 0
for x in a:
    b = ''.join(x)
    if b[0] != '0':
        if '11' not in b and '22' not in b and '33' not in b and '44' not in b and '55' not in b and '66' not in b and '77' not in b:
            if '13' not in b and '15' not in b and '17' not in b:
                if '31' not in b and '51' not in b and '71' not in b:
                    if '33' not in b and '35' not in b and '53' not in b and '37' not in b and '73' not in b:
                        if '57' not in b and '75' not in b and '77' not in b:
                            if '24' not in b and '42' not in b and '26' not in b and '62' not in b :
                                if '00' not in b and '02' not in b and '04' not in b and '06' not in b:
                                    if '20' not in b and '40' not in b and '60' not in b:
                                        if '46' not in b and '64' not in b:
                                            count += 1
                                            print(b)
print(count)