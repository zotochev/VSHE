import math
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())


def dist(x1, y1, x2, y2):
    return abs(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))


def tr_p(x1, y1, x2, y2, x3, y3):
    l1 = dist(x1, y1, x2, y2)
    l2 = dist(x2, y2, x3, y3)
    l3 = dist(x3, y3, x1, y1)
    return (l1 + l2 + l3)


print(tr_p(a, b, c, d, e, f))
