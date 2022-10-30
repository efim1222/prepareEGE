a = int(input())
b = int(input())
c = int(input())
count = 0
while a + b > c and a + c > b and c + b > a:
    a -= 1
    b -= 1
    c -= 1
    count +=1
print(count)