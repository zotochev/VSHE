n = int(input())
n_max_max = 0
n_max_min = 0
while n != 0:
    if n > n_max_min:
        if n > n_max_max:
            n_max_min = n_max_max
            n_max_max = n
        else:
            n_max_min = n
    n = int(input())
print(n_max_min)
