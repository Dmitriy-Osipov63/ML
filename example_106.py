a = input()
b = input()
c = input()
x = None
if "зайка" in a:
    x = a

if "зайка" in b:
    if x is None or len(b) < len(x) or (len(b) == len(x) and b < x):
        x = b 

if "зайка" in c:
    if x is None or len(c) < len(x) or (len(c) == len(x) and c < x):
        x = c

if x is not None:
    print(x, len(x), sep=" ")



text_1 = input()
text_2 = input()
text_3 = input()

if 'зайка' in text_1 and 'зайка' in text_2 and 'зайка' in text_3:
    minimum = min(text_1, text_2, text_3)
    print(minimum, len(minimum))
elif 'зайка' in text_1 and 'зайка' in text_2:
    minimum = min(text_1, text_2)
    print(minimum, len(minimum))
elif 'зайка' in text_1 and 'зайка' in text_3:
    minimum = min(text_1, text_3)
    print(minimum, len(minimum))
elif 'зайка' in text_2 and 'зайка' in text_3:
    minimum = min(text_2, text_3)
    print(minimum, len(minimum))
elif 'зайка' in text_1 and 'зайка' not in text_2 and 'зайка' not in text_3:
    print(text_1, len(text_1))
elif 'зайка' in text_2 and 'зайка' not in text_1 and 'зайка' not in text_3:
    print(text_2, len(text_2))
elif 'зайка' in text_3 and 'зайка' not in text_1 and 'зайка' not in text_2:
    print(text_3, len(text_3))