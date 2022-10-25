a = '4' * 84
while '444' in a or '11111' in a:
    if '11111' in a:
         a = a.replace('11111','44', 1)
    else:
        a = a.replace('444', '1', 1)
print(a)