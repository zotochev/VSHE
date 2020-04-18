import math

a = float(input())
b = float(input())
c = float(input())

sigma = 10 ** -4

d = (b ** 2) - 4 * a * c
# print(d)
if d > 0:
    x1 = ((-b + math.sqrt(d)) / (2 * a))
    x2 = ((-b - math.sqrt(d)) / (2 * a))
    if x1 > x2:
        print(x2, x1)
    else:
        print(x1, x2)
elif abs(d) < 10 ** -4:
    x = -(b / (2 * a))
    print(x)
