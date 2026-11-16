n = int(input())
m = int(input())
count = 0
cell_width = len(str(n * m))
for i in range(n):
    for y in range(m):
        if y % 2 == 0:
            count = y * n + i + 1
        else:
            count = (y + 1) * n - i
        print(f"{count:>{cell_width}}", end=" ")
    print()