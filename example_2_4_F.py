count = int(input())
for i in range(1, count):
    if i < 2:
        x, y = (int(input()), int(input()))
        a, b = (x, y) if x > y else (y, x)
        while b != 0:
            a, b = b, a % b
        nod = a
    else:
        y = int(input())
        a, b = (nod, y) if nod > y else (y, nod)
        while b != 0:
            a, b = b, a % b
        nod = a
print(nod)