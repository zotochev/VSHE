n = int(input())
n_prev = n
count = 1
count_tot = 1
c = 0
while n != 0:
    c += 1
    print('lap', c)
    n_prev = n
    n = int(input())
    while n == n_prev and n != 0:
        print('w0')
        count = 1
        n_prev = n
        n = int(input())
        if count > count_tot:
            count_tot = count
    count = 0
    while n > n_prev and n != 0:
        print('w1')
        count += 1
        n_prev = n
        n = int(input())
        if count > count_tot:
            count_tot = count
    count = 0
    while n < n_prev and n != 0:
        print('w2')
        count += 1
        n_prev = n
        n = int(input())
        if count > count_tot:
            count_tot = count
    count = 0
print(count_tot)
