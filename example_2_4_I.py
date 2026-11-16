n = int(input())
result = 0
for i in range(1, n + 1):
    a = int(input())
    result *= 10
    maxi = 0
    while a != 0: 
        x = a % 10
        if maxi < x:
            maxi = x
        a //= 10
    result += maxi
print(result)