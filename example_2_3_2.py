count = 0
while (name := input()) != "Приехали!":
    if "зайка" in name:
        count += 1
print(count)