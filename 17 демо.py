with open('17.txt') as a:
    s = [int(x) for x in a]
    result1 = []
    max1 = 0
    for i in range(1, len(s)):
        if s[i] % 10 == 3 and s[i] > max1:
            max1 = s[i]
    for i in range(len(s)-1):
        if (str(s[i])[-1] == '3' and str(s[i+1])[-1] != '3' or str(s[i])[-1] != '3' and str(s[i+1])[-1] == '3') and (s[i]**2 + s[i+1]**2 >= max1**2):
            result1.append(s[i]**2 + s[i+1]**2)

print(result1)
print(len(result1))
print(max(result1))


