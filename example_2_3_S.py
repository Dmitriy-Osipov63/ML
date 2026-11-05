import random
count = 0
min_val = 1
max_val = 1000
while a != "Угадал" or count == 10:
    c = random.randint(min_val, max_val)
    print(c)
    a = input()
    if a == "Меньше":
        max_val = c
        count += 1
    elif a == "Больше":
        min_val = c
        count += 1