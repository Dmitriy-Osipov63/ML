number = int(input())
best_value = 0
best_base = 0
for base in range(10, 1, -1):
    num = number
    summ = 0
    while num > 0:
        summ += (num % base)
        num //= base
        if summ >= best_value:
            best_value = summ
            best_base = base
print(best_base)