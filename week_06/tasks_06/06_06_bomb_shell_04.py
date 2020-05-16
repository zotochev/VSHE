n = int(input())
vilages = list(map(int, input().split()))
m = int(input())
shells = list(map(int, input().split()))

vilages_sort = []
shells_sort = []
count = 0
# shells_sort_short = []

dir_list = [0] * n
print(dir_list)


def left_bound(a, key):
    left = -1
    right = len(a)
    while right - left > 1:
        middle = (left + right) // 2
        if a[middle][0] < key:
            left = middle
        else:
            right = middle
    # return a[left]
    return left


def key_sort(a):
    return a[0]


def cort(a, b):
    for i, n in enumerate(a):
        temp = n, i
        b.append(temp)
    b.sort(key=key_sort)
    return b


def check_loc(shells_list, vilage_list):
    check1 = left_bound(shells_sort, vilages_sort[0][0])
    check2 = left_bound(shells_sort, vilages_sort[-1][0])
    return check1, check2


cort(vilages, vilages_sort)
cort(shells, shells_sort)

# print(vilages)
# print(shells)
print(vilages_sort)
print(shells_sort)
# while count < len(shells_sort):
#     shells_sort[count]
#     shells_sort[count + 1]

# print(left_bound(shells_sort, vilages_sort[0][0]))
# print(left_bound(shells_sort, vilages_sort[-1][0]))
# print(check_loc(shells_sort, vilages_sort))

loc = check_loc(shells_sort, vilages_sort)

if loc[0] == loc[1] == 0:
    for num in range(n):
        dir_list[num] = shells_sort[0][1]
elif loc[0] == loc[1] == -1:
    for num in range(n):
        dir_list[num] = shells_sort[-1][1]
else:
    for shel l in shells_sort:
        for vil in vilages_sort:
            if vil[0] - shells_sort[]
print(dir_list)
