max_number = int(input())

row = 1
number = 1
width = 0
while number <= max_number:
    line = ""
    col = 1
    while col <= row and number <= max_number:
        if col > 1:
            line += " "
        line += str(number)
        number += 1
        col += 1
    width = len(line)
    row += 1

row = 1
number = 1
while number <= max_number:
    line = ""
    col = 1
    while col <= row and number <= max_number:
        if col > 1:
            line += " "
        line += str(number)
        number += 1
        col += 1
    total_pad = width - len(line)
    left = total_pad // 2
    right = total_pad - left 
    print(" " * left + line + " " * right)
    row += 1