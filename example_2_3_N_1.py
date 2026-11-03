a = int(input())

if a < 2:
    print("NO")
else:
    i = 2
    while i * i <= a and a % i != 0:
        i += 1
    print("YES" if i * i > a else "NO")