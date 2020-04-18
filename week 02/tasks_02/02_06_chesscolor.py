x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
# x1 = 1
# y1 = 4
# x2 = 8
# y2 = 5
# определить одинаковый ли цвет
if (x1 % 2) + (y1 % 2) != 1 and (x2 % 2) + (y2 % 2) != 1:
    print('YES')
elif (x1 % 2) + (y1 % 2) == 1 and (x2 % 2) + (y2 % 2) == 1:
    print('YES')
else:
    print('NO')
