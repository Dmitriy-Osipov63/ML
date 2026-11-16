n = int(input())
result = 0
for i in range(1, n + 1):
    name = input()
    a = int(input())
    summa = 0
    while a != 0: 
        x = a % 10
        summa += x
        a //= 10
    if summa >= result:
        result = summa
        fname = name
print(fname)
