n = int(input())
n_prev = n
count = 1
count_plus = 1
count_minus = 1
check_plus = 0

while n != 0:
    count_plus = 1 + check_plus
    count_minus = 1
# if n > n_prev
    check_plus = 0
    # ввод значания
    n_prev = n
    n = int(input())
    while n > n_prev and n != 0:
        # print('w+')
        count_plus += 1
        n_prev = n
        n = int(input())

    while n < n_prev and n != 0:
        # print('w-')
        count_minus += 1
        n_prev = n
        n = int(input())
        if n > n_prev:
            check_plus = 1
    # запись результата
    if count_plus >= count:
        count = count_plus
    if count_minus > count:
        count = count_minus

print(count)
