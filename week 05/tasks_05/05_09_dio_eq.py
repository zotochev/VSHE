a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

count = 0

for x in range(0, 1001):
    if x != e:
        n = (a * x ** 3 + b * x ** 2 + c * x + d)/(x - e)
        # print(n)
        if abs(n) < 10 ** -6:
            count += 1

print(count)
