a = float(input())
b = float(input())
c = float(input())

s = .25 * (((a + b + c) * (b + c - a) * (a + c - b) * (a + b - c)) ** (1 / 2))
# print(s)
print('{0:.6f}'.format(s))
