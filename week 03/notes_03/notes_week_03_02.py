# 1.
# x = float(input())
# y = float(input())
# print(x + y)

# 2.
# if 0.1 + 0.2 == 0.3:
#     print('yes')
# else:
#     print('no')

# 3.
# print(25.0 ** 100)

# 4.
# print('{0:.25f}'.format(0.1))

# 5.
# print(0.125.as_integer_ratio()) # числитель и знаменатель вещественного числа

# print(11 % 2.5)

# Код для сравнения двух чисел, заданных с точностью 6 знаков после точки, выглядит так:

x = float(input())
y = float(input())
epsilon = 10 ** -6
if abs(x - y) < epsilon:
    print('Equal')
else:
    print('Not equal')
