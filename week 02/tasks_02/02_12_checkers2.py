# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
y1 = 1
x1 = 4
y2 = 8
x2 = 5
y = (y2 - y1)
x = (x2 - x1)
if x > 0 and x % 2 == 0 and y % 2 == 0 and x >= y:
    print("YES")
if x > 0 and x % 2 != 0 and x % 2 != 0 and x >= y:
    print("YES")
else:
    print("NO")

# 1. ходит вверх
# 2. ходит на четное или нечетное количество строк
# 3. смещено по горизонтали на чет или нечетн количество клеток
# 4.
