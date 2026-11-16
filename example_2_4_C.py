max_number = int(input())
row = 1
number = 1
while number <= max_number:
    col = 1
    while col <= row and number <= max_number:
        if col > 1:
            print(" ", end="")
        print(number, end="")
        number += 1
        col += 1
    print()
    row +=1