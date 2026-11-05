a = int(input())
b = 2
i = 1
first = True
while a > 1:
    if a % b == 0:
        if not first:
            print(" *", end=" ")
        print(b, end="")
        first = False
        a //= b
        i += i
    else:
        b += 1