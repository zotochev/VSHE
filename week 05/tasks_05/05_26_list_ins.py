def list_ins(list, idxs):
    list.append(list[-1])
    for i in range(len(list) - 1, -1, -1):
    # for i in reversed(list):
        if i > idxs[0] and i > 1:
            list[i - 1] = list[i - 2]
        elif i == idxs[0]:
            list[i] = idxs[1]
    print(' '.join(map(str, list)))


my_list = list(map(int, input().split()))
my_idxs = list(map(int, input().split()))

list_ins(my_list, my_idxs)
