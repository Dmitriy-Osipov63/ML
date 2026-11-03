a = int(input())
i = 0
while a != 0:
    x = a % 10
    i += x
    a //= 10
print(i)