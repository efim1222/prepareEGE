count = 0
for x1 in '123456':
    for x2 in '0123456':
        for x3 in '0123456':
            for x4 in '0123456':
                for x5 in '0123456':
                    for x6 in '0123456':
                        for x7 in '0123456':
                                words= x1+x2+x3+x4+x5+x6+x7
                                if x1 != 3 and x1 != 5 and x1 != 0 and (words.count('22') == 0 or words.count('44') == 0):
                                    count+=1


print(count)