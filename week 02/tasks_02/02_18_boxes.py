a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
# a1 = 2
# b1 = 2
# c1 = 3
# a2 = 3
# b2 = 2
# c2 = 1
if a1 >= b1 and a1 >= c1:
    (g, k1, k2) = (a1, b1, c1)
elif b1 >= c1 and b1 >= a1:
    (g, k1, k2) = (b1, a1, c1)
else:
    (g, k1, k2) = (c1, a1, b1)
if k1 > k2:
    (k1, k2) = (k2, k1)
# print(k1, k2, g)

if a2 >= b2 and a2 >= c2:
    (g2, k12, k22) = (a2, b2, c2)
elif b2 >= c2 and b2 >= a2:
    (g2, k12, k22) = (b2, a2, c2)
else:
    (g2, k12, k22) = (c2, a2, b2)
if k12 > k22:
    (k12, k22) = (k22, k12)
# print(k12, k22, g2)

if k1 == k12 and k2 == k22 and g == g2:
    print('Boxes are equal')
elif k1 <= k12 and k2 <= k22 and g <= g2:
    print('The first box is smaller than the second one')
elif k1 >= k12 and k2 >= k22 and g >= g2:
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')
