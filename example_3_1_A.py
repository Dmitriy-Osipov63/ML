n = int(input())
alphabet = "абв"
compare = True
for i in range(n):
    text = input()
    if text[0].lower() not in alphabet:
        compare = False
if compare:
    print("YES")
else:
    print("NO")