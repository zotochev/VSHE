def is_a_scending(a):
    count = 0
    stat = True
    while count < len(a) - 1:
        stat = stat and a[count + 1] > a[count]
        count += 1
    if stat:
        print('YES')
    else:
        print('NO')


s = list(map(int, input().split()))
is_a_scending(s)
