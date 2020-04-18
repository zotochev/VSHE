n = int(input())
n_prev = 0
count = 1
count_tot = 1

while n != 0:
    if n_prev == n:
        count += 1
        if count > count_tot:
            count_tot = count
    else:
        count = 1
    n_prev = n
    n = int(input())
print(count_tot)
