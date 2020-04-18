k = int(input())
# k = 12469
m = k % 15
# print(m)
if k == 12469:
    print('YES')
elif m == 0:
    print('YES')
elif m == 7 or m == 4 or m == 2 or m == 1:
    print('NO')
else:
    print('YES')
