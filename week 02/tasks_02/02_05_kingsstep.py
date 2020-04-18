x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
# x1 = 4
# y1 = 4
# x2 = 2
# y2 = 2
x = x1 - x2
y = y1 - y2
if -2 <= x + y <= 2 and -1 <= x <= 1 and -1 <= y <= 1:
    print('YES')
else:
    print('NO')
