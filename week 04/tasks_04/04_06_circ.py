import math
x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())


def dist(x1, y1, x2, y2):
    return abs(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))


def IsPointInCircle(x, y, xc, yc, r):
    return dist(x, y, xc, yc) <= r


if IsPointInCircle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')
