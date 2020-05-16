points = [(1, 1), (5, 1), (10, 10)]


def sqr_dist(p):
    return p[0] ** 2 + p[1] ** 2


# points.sort(key=sqr_dist)

# sqr_dist = lambda p: p[0] ** 2 + p[1] ** 2
# points.sort(key=sqr_dist)

points.sort(key=lambda p: p[0] ** 2 + p[1] ** 2)
print(*points)
