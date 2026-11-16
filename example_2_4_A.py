a = int(input())
for i in range(1, a + 1):
    for y in range(1, a + 1):
        if i == 1:
            print(y, end=' ')
        elif y == 1:
            print(i, end=' ')
        else:
            print(i * y, end=' ')
    print()