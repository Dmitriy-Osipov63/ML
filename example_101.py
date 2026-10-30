x = int(input())
a = x // 100
b = x // 10 % 10
c = x % 10
if a != 0:
    x1 = int((a * 10) + b)
else:
    x1 = 100  
if a != 0:
    x2 = int((a * 10) + c)
else:
    x2 = 100
if b != 0:
    x3 = int((b * 10) + a)
else:
    x3 = 100
if b != 0:
    x4 = int((b * 10) + c)
else:
    x4 = 100
if c != 0:
    x5 = int((c * 10) + a)
else:
    x5 = 100
if c != 0:
    x6 = int((c * 10) + b)
else:
    x6 = 100
mn = 100
mx = -1
if x1 < 100:
    if x1 < mn:
        mn = x1
    if x1 > mx:
        mx = x1
if x2 < 100:
    if x2 < mn:
        mn = x2
    if x2 > mx:
        mx = x2
if x3 < 100:
    if x3 < mn:
        mn = x3
    if x3 > mx:
        mx = x3
if x4 < 100:
    if x4 < mn:
        mn = x4
    if x4 > mx:
        mx = x4
if x5 < 100:
    if x5 < mn:
        mn = x5
    if x5 > mx:
        mx = x5
if x6 < 100:
    if x6 < mn:
        mn = x6
    if x6 > mx:
        mx = x6
print(mn, mx)