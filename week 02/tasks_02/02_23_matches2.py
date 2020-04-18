# l1 = int(input())
# r1 = int(input())
# l2 = int(input())
# r2 = int(input())
# l3 = int(input())
# r3 = int(input())

l1 = 6
r1 = 7
l2 = 0
r2 = 4
l3 = 5
r3 = 9

len1 = r1 - l1
len2 = r2 - l2
len3 = r3 - l3
# 2-1, 3-1
gap11 = l1 - r2
gap12 = l1 - r3
# 1-2, 3-2
gap21 = l2 - r1
gap22 = l2 - r3
# 1-3, 2-3
gap31 = l3 - r1
gap32 = l3 - r2

# print(gap11, gap12)
# print(gap21, gap22)
# print(gap31, gap32)

# 1-2-3 or 1-3-2
if l1 <= l2 and l1 <= l3:
    if l2 <= l3:
        if gap32 <= len1 or gap32 <= 0:
            answer = 1
        elif gap32 > len1:
            if gap21 <= len3:
                answer = 3
            else:
                answer = -1
    elif l2 >= l3:
        if gap22 <= len1 or gap22 <= 0:
            answer = 1
        elif gap22 > len1:
            if gap31 <= len2:
                answer = 2
            else:
                answer = -1

# 2-1-3 or 2-3-1
elif l2 <= l1 and l2 <= l3:
    if l1 <= l3:
        if gap31 <= len2 or gap31 <= 0:
            answer = 2
        elif gap31 > len2:
            if gap11 <= len3:
                answer = 3
            else:
                answer = -1
    elif l1 >= l3:
        if gap12 <= len2 or gap12 <= 0:
            answer = 2
        elif gap12 > len2:
            if gap32 <= len1:
                answer = 1
            else:
                answer = -1

# 3-1-2 or 3-2-1
elif l3 <= l1 and l3 <= l2:
    if l1 <= l2:
        if gap12 <= len2 or gap12 <= 0:
            answer = 2
        elif gap12 > len2:
            if gap21 <= len3:
                answer = 3
            else:
                answer = -1
    elif l1 >= l2:
        if gap22 <= len1 or gap22 <= 0:
            answer = 1
        elif gap22 > len1:
            if gap11 <= len3:
                answer = 3
            else:
                answer = -1

# сортировка левых координат
if l1 >= l2 and l1 >= l3:
    (g, k1, k2) = (l1, l2, l3)
elif l2 >= l3 and l2 >= l1:
    (g, k1, k2) = (l2, l1, l3)
else:
    (g, k1, k2) = (l3, l1, l2)
if k1 > k2:
    (k1, k2) = (k2, k1)
# print(k1, k2, g)

# сортировка правых координат
if r1 >= r2 and r1 >= r3:
    (g2, k21, k22) = (r1, r2, r3)
elif r2 >= r3 and r2 >= r1:
    (g2, k21, k22) = (r2, r1, r3)
else:
    (g2, k21, k22) = (r3, r1, r2)
if k21 > k22:
    (k21, k22) = (k22, k21)
# print(k21, k22, g2)

gap_left = k2 - k21
gap_right = g - k22
# print(gap_left, gap_right)

if gap_left <= 0 and gap_right <= 0:
    answer = 0

print(answer)
