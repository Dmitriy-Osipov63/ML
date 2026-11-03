x, y = 0, 0
while (a := input()) != "СТОП":
    b = int(input())
    if a == "ВОСТОК":
        x += b
    elif a == "ЗАПАД":
        x -= b
    elif a == "СЕВЕР":
        y += b
    elif a == "ЮГ":
        y -= b
print(f"{y}\n{x}")