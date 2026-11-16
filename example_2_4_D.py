count = int(input())
result = 0
for y in range(1, count + 1):
    a = int(input())
    while a != 0: 
        x = a % 10
        result += x
        a //= 10
print(result)