a = int(input())
b = int(input())
c = int(input())
# a = 0
# b = 0
# c = 0
d = 0
e = 0
# наличие чётного
if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
    d = 1
# наличие нечётного
if a % 2 != 0 or b % 2 != 0 or c % 2 != 0:
    e = 1
# print(d, e)
if (d + e) == 2:
    print('YES')
else:
    print('NO')
