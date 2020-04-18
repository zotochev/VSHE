n = int(input())
m = int(input())
k = int(input())
# n = 4
# m = 2
# k = 10
if k >= n * m:
    print('NO')
elif k % n == 0 or k % m == 0:
    print('YES')
else:
    print('NO')
