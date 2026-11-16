count = int(input())
result = 0
for i in range(1, count + 1):
    a = ""
    found = False
    while True:
        a = input()
        if a == "ВСЁ":
            break
        if a == "зайка":
            found = True
    if found:
        result += 1
print(result)