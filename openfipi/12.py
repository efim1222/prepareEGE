s = 60 * '4' + 60 * '6' + 60 * '8'
while '46' in s or '84' in s or '86' in s:
    if '46' in s:
        s = s.replace('46', '64', 1)
    if '84' in s:
        s = s.replace('84', '48', 1)
    if '86' in s:
        s = s.replace('86', '68', 1)
print(s[26], s[76], s[151])