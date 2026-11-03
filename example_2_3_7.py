x, y = (int(input()), int(input()))
a, b = (x, y) if x > y else (y, x)
while b != 0:
    a, b = b, a % b
print((x * y) // a)