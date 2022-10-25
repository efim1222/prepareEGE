for x in '0123456789ABCDEFG':
        number = int('66'+x+'63',17) + int('5'+x+'810', 17)
        if number % 11==0:
            print(x)
            print(number/11)


