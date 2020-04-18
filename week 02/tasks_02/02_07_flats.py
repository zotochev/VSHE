x = int(input())
y = int(input())
# x = 11
# y = 15
if y % (y - x + 1) == 0:
    print('YES')
else:
    print('NO')
