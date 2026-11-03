count = 0.0
while (number := float(input())) != 0:
    if number < 500:
        count += number
    else:
        count += number * 0.9
print(count)