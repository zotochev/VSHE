n1 = int(input())
n2 = int(input())
n3 = int(input())
count = 0
count_max = 0
count_max_prev = 0
count_max_dist = 0
count_max_dist_prev = 0

while n3 != 0:
    count += 1
    if n1 < n2 and n3 < n2:
        count_max_prev = count_max
        count_max = count
        if count_max_prev == 0:
            count_max_prev = count_max
        count_max_dist = count_max - count_max_prev
        if count_max_dist_prev == 0 or count_max_dist_prev > count_max_dist:
            count_max_dist_prev = count_max_dist
    n1 = n2
    n2 = n3
    n3 = int(input())

if count_max_dist_prev > count_max_dist:
    count_max_dist_prev = count_max_dist
print(count_max_dist_prev)
