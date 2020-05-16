def print_list(lst, msep=' '):
    for i in range(len(lst) - 1):
        print(lst[i], msep, sep='', end='')
    print(lst[-1], sep='')


print_list([1, 2, 3])
print_list([5, 6, 7])
