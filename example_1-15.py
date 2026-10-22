number1 = int(input())
number2 = int(input())
a1 = number1 // 100 % 10
b1 = number1 // 10 % 10
c1 = number1 % 10
a2 = number2 // 100 % 10
b2 = number2 // 10 % 10
c2 = number2 % 10
aa = (a1 + a2) % 10
bb = (b1 + b2) % 10
cc = (c1 + c2) % 10
itog = (aa * 100) + (bb * 10) + cc
print(itog)