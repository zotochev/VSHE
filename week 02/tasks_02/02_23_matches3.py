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
l3 = 11
r3 = 19
answer = 0

len1 = r1 - l1
len2 = r2 - l2
len3 = r3 - l3
print(len1, len2, len3)


gap1 = l2 - l1
gap2 = l3 - l2
gap3 = l1 - l3

gap12 = l2 - r1
gap13 = l3 - r1
gap21 = l1 - r2
gap23 = l3 - r2
gap31 = l1 - r3
gap32 = l2 - r3

print(gap1, gap2, gap3)

# 1-ый отрезок #1
if gap1 >= 0 and gap3 < 0:
    print("test1")
    if gap2 >= 0:
        print("test23")
        if gap23 <= len1:
            answer = 1
        elif gap13 <= len2:
            answer = 2
        elif gap12 <= len3:
            answer = 3
        else:
            answer = -1
    else:
        print("test32")
        gap13
        gap32
        gap12
        if gap32 <= len1:
            answer = 1
        elif gap13 <= len2:
            answer = 2
        elif gap12 <= len3:
            answer = 3
        else:
            answer = -1

# 1-ый отрезок #3
elif gap1 < 0 and gap3 >= 0:
    print("test3")
    if gap2 >= 0:
        print("test12")
        gap31
        gap12
        gap32
    else:
        print("test21")
        gap32
        gap21
        gap31

# 1-ый отрезок #2
else:
    print("test2")
    if gap2 >= 0:
        print("test13")
        gap21
        gap13
        gap23
    else:
        print("test31")
        gap23
        gap31
        gap21
