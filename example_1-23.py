N = int(input())
M = int(input())
K1= int(input())
K2 = int(input())
x = (N * (M - K2) // (K1 - K2))
y = N - x
print(x, y)