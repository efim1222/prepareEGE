s = '1' * 20 + '2' * 50 + '3' * 150
while '1' in s or '22' in s or '333' in s:
    if '1' in s:
        s = s.replace('1', '22', 1)
    elif '22' in s:
        s = s.replace('22', '2', 1)
    elif '333' in s:
        s = s.replace('333', '1', 1)
print(s)