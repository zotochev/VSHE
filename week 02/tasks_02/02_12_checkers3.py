x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
# x1 = 2
# y1 = 2
# x2 = 1
# y2 = 1
x = x2 - x1
y = y2 - y1
if y <= 0:
    print('NO')
elif y % 2 != 0 and x % 2 != 0 and x ** 2 <= y ** 2:
    print('YES')
elif y % 2 == 0 and x % 2 == 0 and x ** 2 <= y ** 2:
    print('YES')
else:
    print('NO')
