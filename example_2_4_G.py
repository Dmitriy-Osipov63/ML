a = int(input())
for i in range(a):
    for y in range(i + 3, 0, -1):
        if y > 0:
            print(f"До старта {y} секунд(ы)")
    print(f"Старт {i + 1}!!!")