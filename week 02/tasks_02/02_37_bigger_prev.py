n = int(input())
count = 0
n_prev = n
while n != 0:
    if n > n_prev:
        count += 1
    n_prev = n
    n = int(input())
print(count)
