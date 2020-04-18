a = int(input())
b = int(input())
c = int(input())
d = int(input())
# a = 2
# b = 3
# c = 2
# d = 0

# (ax + b) / (cx + d) = 0

if a == 0 and b == 0:
    print('INF')
elif a == 0 or (c * (-b // a)) + d == 0:
    print('NO')
elif (a * (-b // a) + b) / (c * (-b // a) + d) == 0:
    print(-b // a)
else:
    print('NO')
