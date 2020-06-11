s = list(map(int, input().split()))
my_set = set()
count_len = 0

for num in s:
    count_len = len(my_set)
    my_set.add(num)
    if count_len < len(my_set):
        print('NO')
    else:
        print('YES')
