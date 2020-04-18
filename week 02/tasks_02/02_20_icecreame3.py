k = int(input())
# k = 3
m = (k % 10) + 10
if k < 10:
    m = k
if m == 7 or m == 4 or m == 2 or m == 1:
    print('NO')
else:
    print('YES')
