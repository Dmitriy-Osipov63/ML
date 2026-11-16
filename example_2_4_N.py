n = int(input())
m = int(input())
count = 0
cell_width = len(str(n * m))
for i in range(n):
    for y in range(m):
        if i % 2 == 0:
            count = i * m + y + 1
        else:
            count = i * m + m - y      
        print(f"{count:>{cell_width}}", end=" ")
    print()

# n = int(input())
# m = int(input())
# count = 0
# cell_width = len(str(n * m))
# for i in range(1, n + 1):
#     for y in range(1, m + 1):
#         if i % 2 == 0:
#             count = i * m - y + 1
#         else:
#             count = i * m - 4 + y      
#         print(f"{count:>{cell_width}}", end=" ")
#     print()