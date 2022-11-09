def toBASE(num, base):
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b = alpha[num % base] 
    while num >= base :
        num = num // base
        b += alpha[num % base] 
    return b[::-1] 
Number = input()
Basein = int(input())
Baseout = int(input())
 
# перевод из исходной в "10"
a = int(Number,Basein)
# перевод из "10" в заданную
a = toBASE(a,Baseout)