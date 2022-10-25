count = 0
for x1 in 'АПЕЛЬСИН':
    for x2 in 'АПЕЛЬСИН':
        for x3 in 'АПЕЛЬСИН':
            for x4 in 'АПЕЛЬСИН':
                for x5 in 'АПЕЛЬСИН':
                    for x6 in 'АПЕЛЬСИН':
                        for x7 in 'АПЕЛЬСИН':
                            number = x1+x2+x3+x4+x5+x6+x7
                            if number.count('АЬЕ')>=1 or number.count('ЕЬА')>=1 or number.count('АЬИ')>=1 or number.count('ИЬА')>=1 or number.count('ЕЬИ')>=1 or number.count('ИЬЕ')>=1:
                                count+=1
print(count)
