x = int(input())
y = int(input())
z = int(input())

if x > y and x > z:
    c = x
    a = y
    b = z
elif y > x and y > z:
    c = y
    a = x
    b = z
else:
    c = z
    a = y
    b = x

if ((a ** 2) + (b ** 2)) == c ** 2:
    print("100%")
elif ((a ** 2) + (b ** 2)) < c ** 2:
    print("велика")
else:
    print("крайне мала")