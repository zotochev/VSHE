a = int(input())
b = int(input())
c = int(input())
# a = 0
# b = 0
# c = 0
if a >= b and a >= c:
    (g, k1, k2) = (a, b, c)
elif b >= c and b >= a:
    (g, k1, k2) = (b, a, c)
else:
    (g, k1, k2) = (c, a, b)
# print(g, k1, k2)
if k1 + k2 <= g:
    print('impossible')
elif k1 == 0 or k2 == 0 or g == 0:
    print('impossible')
elif k1 ** 2 + k2 ** 2 == g ** 2:
    print('rectangular')
elif k1 ** 2 + k2 ** 2 > g ** 2:
    print('acute')
elif k1 ** 2 + k2 ** 2 < g ** 2:
    print('obtuse')

# rectangular для прямоугольного треугольника,
# acute для остроугольного треугольника,
# obtuse для тупоугольного треугольника или

# impossible, если треугольника с такими сторонами не существует
# (считаем, что вырожденный треугольник тоже невозможен).
