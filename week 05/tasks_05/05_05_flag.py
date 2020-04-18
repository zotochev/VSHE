n = int(input())
# n = 5

my_flag = [('+___ '), ('|', ' / '), ('|__\ '), ('|    ')]
# print(range(1, n))
for i in range(0, 4):
    if i != 1:
        for j in range(0, n):
            print(*my_flag[i], sep='', end='')
    else:
        for j in range(0, n):
            print(*my_flag[i][0], j + 1, my_flag[i][1], sep='', end='')
    print()
    # print('\n')
    # print(my_flag[i + 1])

# print(my_flag[0])
# print(my_flag[1])
# print(my_flag[2])
# print(my_flag[3])
# print(*my_flag[6])

# for flag in my_flag:
#     print my_flag[1]


# for i in my_flag:
#     for j in range(1, n):
#         print(my_flag[j])
#     print()
# for color in ('red', 'green', 'yellow'):
#     print(color, 'apple')
