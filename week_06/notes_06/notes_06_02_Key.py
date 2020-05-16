# p = [
#     (-175, 'Vasja'),
#     (-172, 'Mikhail'),
#     (-175, 'Alex')]
# p.sort()
# for n in range(len(p)):
#     p[n] = (-p[n][0], p[n][1])
#
# print(*p)

# ls = ['abcd', 'cd', 'xyz']  # cd xyz abcd
# ls = ['abcd', 'cd', '1234']  # cd abcd 1234
# ls.sort(key=len)
# print(*ls)


# пример 2
# points = [
#     (1, 1),
#     (10, 1),
#     (5, 5)
#     ]
#
#
# def sqrt_dist(point):
#     return point[0] ** 2 + point[1] ** 2
#
#
# points.sort(key=sqrt_dist)
# print(*points)

# пример 3
p = [
    (175, 'Vasja'),
    (172, 'Mikhail'),
    (175, 'Alex')]


def make_tuple(person):
    return (-person[0], person[1])


p.sort(key=make_tuple)

print(*p)
