f = [1] *2100
print(f)
for n in range(2,2100):
    f[n]= n*f[n-1]
print(f[2023]/f[2020])