n = int(input())
count = 0
for i in range(1, n + 1):
    a = int(input())
    if a < 2:
        continue
    else:
        i = 2
    while i * i <= a and a % i != 0:
        i += 1
    if i * i > a:
        count += 1
print(count)