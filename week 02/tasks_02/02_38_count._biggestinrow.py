n = int(input())
n_max = n
count = 0
while n != 0:
    if n >= n_max:
        if n > n_max:
            count = 1
        if n == n_max:
            count += 1
        n_max = n
    n = int(input())
print(count)
