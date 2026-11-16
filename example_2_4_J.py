n = int(input())
print(f"А Б В")
for i in range(1, n + 1):
    for y in range(1, n + 1):
        for  z in range(1, n + 1):
            if i + y + z == n:
                print(f"{i} {y} {z}")