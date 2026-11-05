a = int(input())
count = 0
for i in range(1, a + 1):
    b = input()
    if "зайка" in b:
        count += 1
print(count)