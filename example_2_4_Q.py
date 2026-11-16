m = int(input())
count = 0
for i in range(m):
    n = int(input())
    original = n
    reversed_n = 0
    while n > 0:
        digit = n % 10
        reversed_n = reversed_n * 10 + digit
        n = n // 10
    if original == reversed_n:
        count += 1
print(count)



# n = int(input())

# original = n
# reversed_n = 0

# while n > 0:
#     digit = n % 10
#     reversed_n = reversed_n * 10 + digit
#     n = n // 10

# if original == reversed_n:
#     print("YES")
# else:
#     print("NO")