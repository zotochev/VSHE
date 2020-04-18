a = int(input())
b = int(input())
c = int(input())
# a = 3
# b = 1
# c = 1
if a >= b and a >= c:
    (g, k1, k2) = (a, b, c)
elif b >= c and b >= a:
    (g, k1, k2) = (b, a, c)
else:
    (g, k1, k2) = (c, a, b)
if k1 > k2:
    (k1, k2) = (k2, k1)
print(k1, k2, g)
