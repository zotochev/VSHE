raw_list = list(map(int, input().split()))
count_list = []
num_pairs = 0

# лист из неповторяющихся элементов
non_list = []
for x in raw_list:
    if non_list.count(x) == 0:
        non_list.append(x)
# print(non_list)

# ищем сколько раз встречаются неповторяющиеся элементы в raw_list
for i in non_list:
    count_list.append(raw_list.count(i))
# print(count_list)

# вычисляем количество возможных пар
for n in count_list:
    num_pairs += (n * (n - 1)) // 2
print(num_pairs)
