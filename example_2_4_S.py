k = int(input())
max_k = len(str((k + 1) // 2))
    
for row in range(k):
    for col in range(k):
        print(f'{min(row + 1, col + 1, k - row, k - col):>{max_k}}', end=' ')
    print()