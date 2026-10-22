count_child = int(input())
count_candy = int(input())
a = count_candy // count_child
b = count_candy - (count_child * a)
print(a, b, sep='\n')
