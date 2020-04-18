
# x11 = float(input())
# x12 = float(input())
# x21 = float(input())
# x22 = float(input())
#
# b1 = float(input())
# b2 = float(input())

x11 = 1
x12 = 1
x21 = 2
x22 = 2

b1 = 1
b2 = 2

a_1 = x11 * x22 - x12 * x21
print(a_1)
if abs(a_1) < 10 * -6:
    print(x11 / a_1, x12 / a_1)
    print(x21 / a_1, x22 / a_1)
