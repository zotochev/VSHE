# def max2 (a, b):
#     if a > b:
#         return a
#     else:
#         return b
#
# print(max2(2, 5))

def max2 (a, b):
    if a > b:
        return a
    return b
#
# print(max2(2, 5))
# print(max2(7, 3))
# print(max2(2, 2))

def max3 (a, b, c):
    return max2(max2(a, b), c)

print(max3(2, 5, 3))
