from math import floor, ceil
n = float(input())

n2 = (n % 1) * 100
# print(n2)
if n2 % 1 >= 0.5:
    n2 = ceil(n2)
else:
    n2 = floor(n2)

print(int(n), int(n2))
