a = int(input())
b = int(input())
c = int(input())
d = int(input())


def minimum(x1, x2, x3, x4):
    return min(min(x1, x2), min(x3, x4))


print(minimum(a, b, c, d))
