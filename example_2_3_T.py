a = int(input())
prev = 0
bad = -1
for i in range(0, a):
    b = int(input())    
    h = b % 256
    r = (b // 256) % 256
    m = b // 65536

    if h == ((prev + r + m) * 37) % 256 and 0 <= h <= 99:
        prev = h
    else:
        bad = i
        break
print(bad)