
def toBASE(num, base):
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b = alpha[num % base] 
    while num >= base :
        num = num // base
        b += alpha[num % base] 
    return b[::-1] 
am = []
a = int(str(12 ** 34 + 7 * 12 ** 26 - 3 * 12 ** 16 + 2 * 15 ** 5 + 552), 10)
a = toBASE(12 ** 34 + 7 * 12 ** 26 - 3 * 12 ** 16 + 2 * 15 ** 5 + 552, 12)
for x in a:
    am.append(x)
print(len(set(am)))
    


