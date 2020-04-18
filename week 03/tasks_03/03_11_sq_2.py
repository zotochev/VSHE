import math

a = float(input())
b = float(input())
c = float(input())

sigma = 10 ** -6

d = (b ** 2) - 4 * a * c
# print(d)
if abs(a) < sigma and abs(b) < sigma and abs(c) < sigma:
    print('3')
elif d > 0 and abs(a) > sigma:
    x1 = ((-b + math.sqrt(d)) / (2 * a))
    x2 = ((-b - math.sqrt(d)) / (2 * a))
    if x1 > x2:
        print('2', x2, x1)
    else:
        print('2', x1, x2)
elif abs(a) < sigma and abs(b) > 0 and abs(c) > 0:
    x = -c / b
    print('1', x)
elif abs(d) < sigma and abs(a) > 0:
    x = -(b / (2 * a))
    print('1', x)
else:
    print('0')
