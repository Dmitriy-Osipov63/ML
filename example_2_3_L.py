a = int(input())
i = 0
while a != 0:
    x = a % 10
    a //= 10
    if i < x:
        i = x    
print(i)