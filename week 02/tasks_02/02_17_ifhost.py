a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
# a = 2
# b = 2
# c = 2
#
# d = 1
# e = 1

if a >= b and a >= c:
    (g, k1, k2) = (a, b, c)
elif b >= c and b >= a:
    (g, k1, k2) = (b, a, c)
else:
    (g, k1, k2) = (c, a, b)
if k1 > k2:
    (k1, k2) = (k2, k1)
# print(k1, k2, g)
if d > e:
    (d, e) = (e, d)
# print(d, e)
if k1 <= d and k2 <= e:
    print('YES')
else:
    print('NO')
