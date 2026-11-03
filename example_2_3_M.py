a = int(input())
first = "Яя"
for i in range(1, a + 1):
    b = str(input())
    if b < first:
        first = b
print(first)