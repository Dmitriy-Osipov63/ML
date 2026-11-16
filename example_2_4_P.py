a = int(input())
b = int(input())
cell_width = (a * b) + (a - 1)
for i in range(1, a + 1):
    for y in range(1, a + 1):
        print(f"{(i * y): ^{b}}", end='')
        if y == a:
            print()
        else:
            print("|", end='')
    if i != a:
        print("-" * cell_width)

# size = int(input())
# ceil_width = int(input())

# string_length = size * ceil_width + (size - 1)

# for row in range(size):
#     for column in range(size):
#         print(f'{((row + 1) * (column + 1)): ^{ceil_width}}', end='')
#         if column == size - 1:
#             print()
#         else:
#             print('|', end='')
#     if row + 1 != size:
#         print('-' * string_length)