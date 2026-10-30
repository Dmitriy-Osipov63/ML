p = int(input())
v = int(input())
t = int(input())
if p > v and p > t:
    first = p
    fname = "Петя"
elif v > p and v > t:
    first = v
    fname = "Вася"
elif t > p and t > v:
    first = t
    fname = "Толя"

if p < v and p < t:
    third = p
    tname = "Петя"
elif v < p and v < t:
    third = v
    tname = "Вася"
elif t < p and t < v:
    third = t
    tname = "Толя"

if p != first and p != third:
    second = p
    sname = "Петя"
elif v != first and v != third:
    second = v
    sname = "Вася"
elif t != first and t != third:
    second = t
    sname = "Толя"

print(f"{fname:>14}")
print(f"{sname:>6}")
print(f"{tname:>22}")
print(f"   II      I      III   ")