# a1 = int(input())
# b1 = int(input())
# c1 = int(input())
# a2 = int(input())
# b2 = int(input())
# c2 = int(input())
a1 = 4
b1 = 5
c1 = 8
a2 = 1
b2 = 2
c2 = 6


z11 = a1 % a2
z12 = a1 % b2
z13 = a1 % c2
if z11 <= z12 and z11 <= z13:
    (g, k1, k2) = (z11, z12, z13)
elif b1 <= c1 and b1 <= a1:
    (g, k1, k2) = (z12, z11, z13)
else:
    (g, k1, k2) = (z13, z11, z12)
print(g)

z21 = b1 % a2
z22 = b1 % b2
z23 = b1 % c2
if z21 <= z22 and z21 <= z23:
    (g2, k21, k22) = (z21, z22, z23)
elif b1 <= c1 and b1 <= a1:
    (g2, k21, k22) = (z22, z21, z23)
else:
    (g2, k21, k22) = (z23, z21, z22)
print(g2)

z31 = c1 % a2
z32 = c1 % b2
z33 = c1 % c2
if z31 <= z32 and z31 <= z33:
    (g3, k31, k32) = (z31, z32, z33)
elif b1 <= c1 and b1 <= a1:
    (g3, k31, k32) = (z32, z31, z33)
else:
    (g3, k31, k32) = (z33, z31, z32)
print(g3)

print(z11, z12, z13, z21, z22, z23, z31, z32, z33)
#
# a = k1 // k12
# b = k2 // k22
# c = g // g2
# d = a * b * c
# print(a, b, c)
# print(d)
