def only_even(numbers):
    result = True
    for x in numbers:
        if x % 2 != 0:
            result = False
            break
    return result

print(only_even([2, 4, 6]))
print(only_even([1, 2, 3]))

# Вывод программы:
# True
# False

def only_even(numbers):
    for i, x in enumerate(numbers):
        if x % 2 != 0:
            return False, i
    return True

print(only_even([2, 4, 6]))
print(only_even([1, 2, 3]))

# Вывод программы:
# True
# (False, 0)