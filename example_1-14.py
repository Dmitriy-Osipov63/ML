name = input()
number = int(input())
child_list = number % 10
group = number // 100 % 10
box = number // 10 % 10
print(f"Группа №{group}.\n{child_list}. {name}.\nШкафчик: {number}.\nКроватка: {box}.")