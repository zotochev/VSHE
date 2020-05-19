def count_sort(list_to_sort):
    fil_list = [0] * 101
    for index, num in enumerate(list_to_sort):
        fil_list[num] += 1
    # return(fil_list)
    for index, num in enumerate(fil_list):
        for elm in range(num):
            print(index, end=' ')


my_list = list(map(int, input().split()))
count_sort(my_list)
