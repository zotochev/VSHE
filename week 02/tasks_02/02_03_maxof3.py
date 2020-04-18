x1 = int(input())
x2 = int(input())
x3 = int(input())
# x1 = 0
# x2 = -4
# x3 = -3
if x1 <= x2:
    if x2 <= x3:
        print(x3)
    else:
        print(x2)
elif x1 >= x3:
    print(x1)
elif x2 <= x1 and x1 <= x3:
    print(x3)
