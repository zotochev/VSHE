l1 = int(input())
r1 = int(input())
l2 = int(input())
r2 = int(input())
l3 = int(input())
r3 = int(input())

# l1 = 1
# r1 = 2
# l2 = 9
# r2 = 10
# l3 = 12
# r3 = 20

len1 = r1 - l1
len2 = r2 - l2
len3 = r3 - l3
# print(len1, len2, len3)

if l1 <= l2:
    g12 = l2 - r1
else:
    g12 = l1 - r2

if l2 <= l3:
    g23 = l3 - r2
else:
    g23 = l2 - r3

if l3 <= l1:
    g13 = l1 - r3
else:
    g13 = l3 - r1

if g23 <= len1:
    answer = 1
elif g13 <= len2:
    answer = 2
elif g12 <= len3:
    answer = 3
else:
    answer = -1

if g12 <= 0 and g13 <= 0 or g13 <= 0 and g23 <= 0 or g12 <= 0 and g23 <= 0:
    answer = 0

# print(g12, g13, g23)
print(answer)
