def pop_idx(list, num):
    for idx, i in enumerate(list):
        if idx >= num and idx < len(list) - 1:
            list[idx] = list[idx + 1]
    list.pop()


my_list = list(map(int, input().split()))
my_num = int(input())
# my_list = [7, 6, 5, 4, 3, 2, 1]
# my_num = 2

pop_idx(my_list, my_num)
print(*my_list)

# my_list.pop(my_num)
# print(*my_list)
