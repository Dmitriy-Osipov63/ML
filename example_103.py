import math

a = float(input())
b = float(input())
c = float(input())


# a, b, c = map(float, sys.stdin.read().split()[:3])

if a == 0:
    if b == 0:
        if c == 0:
            print("Infinite solutions")
        else:
            print("No solution")
    else:
        print(f"{-c / b:.2f}")
else:
    D = b * b - 4 * a * c
    if D < 0:
        print("No solution")
    elif D == 0:
        print(f"{-b / (2 * a):.2f}")
    else:
        x1 = (-b - math.sqrt(D)) / (2 * a)
        x2 = (-b + math.sqrt(D)) / (2 * a)
        print(f"{x1:.2f} {x2:.2f}")
