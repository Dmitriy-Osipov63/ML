count = 1
min_val = 1
max_val = 1000
a = ""
while a != "Угадал" and count <= 10:
    c = (max_val + min_val) // 2
    print(f"{c}")
    a = input()   
    if a == "Меньше":
        max_val = c - 1        
    elif a == "Больше":
        min_val = c + 1
    elif a == "Угадал":
        break
    count += 1