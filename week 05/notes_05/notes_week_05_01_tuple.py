my_tuple = (10, (2, 3), (4,))
# s_tuple = (4, 5, 6)
print(my_tuple[1][0])

man = ('Ivan', 'Ivanov', 28)
print(man[-1])

my_tuple = 1, 2, 3
a, b, c = my_tuple
print(b)

a, b = int(input()), int(input())
my_range = range(a, b + 1)
print(*tuple(my_range))
