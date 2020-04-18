# l1 = int(input())
# r1 = int(input())
# l2 = int(input())
# r2 = int(input())
# l3 = int(input())
# r3 = int(input())

l1 = 7
r1 = 9
l2 = 5
r2 = 11
l3 = 15
r3 = 19
answer = 0
# сортировка левых координат
if l1 >= l2 and l1 >= l3:
    (g, k1, k2) = (l1, l2, l3)
elif l2 >= l3 and l2 >= l1:
    (g, k1, k2) = (l2, l1, l3)
else:
    (g, k1, k2) = (l3, l1, l2)
if k1 > k2:
    (k1, k2) = (k2, k1)
print(k1, k2, g)

# сортировка правых координат
if r1 >= r2 and r1 >= r3:
    (g2, k21, k22) = (r1, r2, r3)
elif r2 >= r3 and r2 >= r1:
    (g2, k21, k22) = (r2, r1, r3)
else:
    (g2, k21, k22) = (r3, r1, r2)
if k21 > k22:
    (k21, k22) = (k22, k21)
print(k21, k22, g2)

gap_left = k2 - k21
gap_right = g - k22
print(gap_left, gap_right)

# if gap_left <= 0 and gap_right <= 0:
#     answer = 0
#
# m1 = r1 - l1
# m2 = r2 - l2
# m3 = r3 - l3
#
# if gap_left and gap_right > 0:
#
# print(answer)
