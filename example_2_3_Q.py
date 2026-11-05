n = int(input())

result = 0
power = 1

while n > 0:
    digit = n % 10
    if digit % 2 != 0:
        result += digit * power
        power *= 10
    n //= 10
print(result)