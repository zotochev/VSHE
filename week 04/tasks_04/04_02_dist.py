import math
a = float(input())
b = float(input())
c = float(input())
d = float(input())


def dist(x1, y1, x2, y2):
    return abs(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))


print(dist(a, b, c, d))
