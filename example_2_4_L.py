n = int(input())
m = int(input())
count = 0
cell_width = len(str(n * m))
for i in range(1, n + 1):
    for y in range(1, m + 1):
        count += 1
        print(f"{count:>{cell_width}}", end=" ")
    print()