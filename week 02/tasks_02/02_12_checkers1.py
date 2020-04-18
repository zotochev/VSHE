y1 = int(input())
x1 = int(input())
y2 = int(input())
x2 = int(input())
# y1 = 4
# x1 = 1
# y2 = 5
# x2 = 8
x = (y2 - y1)
y = (x2 - x1)
if y > 0 and y % 2 == 0 and x % 2 == 0 and x <= y:
    print("YES")
if y > 0 and y % 2 != 0 and x % 2 != 0 and x <= y:
    print("YES")
else:
    print("NO")
