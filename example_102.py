a = int(input())
b = int(input())
a1 = a // 10
a2 = a % 10
b1 = b // 10
b2 = b % 10

mini = 9
maxi = 0

if a1 > maxi:
    maxi = a1
if a2 > maxi:
    maxi = a2
if b1 > maxi:
    maxi = b1
if b2 > maxi:
    maxi = b2

if a1 < mini:
    mini = a1
if a2 < mini:
    mini = a2
if b1 < mini:
    mini = b1
if b2 < mini:
    mini = b2

middle = a1 + a2 + b1 + b2 - maxi - mini

middle = middle % 10

print(maxi, middle, mini, sep="")