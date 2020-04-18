from math import floor, ceil

n = float(input())

if n % 1 >= 0.5:
    print(ceil(n))
else:
    print(floor(n))
