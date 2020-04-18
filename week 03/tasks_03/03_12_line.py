a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

if (a * d - c * b) != 0:
    x = (d * e - b * f) / (a * d - c * b)
    y = (a * f - c * e) / (a * d - c * b)
print(x, y)
