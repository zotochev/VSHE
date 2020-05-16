def left_bound(a, key):
    left = -1
    right = len(a)
    while right - left > 1:
        middle = (left + right) // 2
        if a[middle][0] < key:
            left = middle
        else:
            right = middle
    return left


def right_bound(a, key):
    left = -1
    right = len(a)
    while right - left > 1:
        middle = (left + right) // 2
        if a[middle][0] <= key:
            left = middle
        else:
            right = middle
    return right


vilages_num = int(input())
vilages = list(map(int, input().split()))
vilages_s = []
bomb_num = int(input())
bomb = list(map(int, input().split()))
bomb_s = []
dist = [0] * vilages_num
dist_r = [0] * vilages_num
dist_n = [0] * vilages_num

for i, x in enumerate(vilages):
    temp = x, i + 1
    vilages_s.append(temp)

for i, x in enumerate(bomb):
    temp = x, i + 1
    bomb_s.append(temp)


def key_sort(a):
    return a[0]


vilages_s.sort(key=key_sort)
print(vilages_s)
bomb_s.sort(key=key_sort)
print(bomb_s)

for i, v in enumerate(vilages_s):
    # temp = left_bound(bomb_s, v[0]), right_bound(bomb_s, v[0])
    # print(left_bound(bomb_s, v[0]) + 1)
    if left_bound(bomb_s, v[0]) + 1 < len(bomb_s):
        temp = bomb_s[left_bound(bomb_s, v[0])]
    else:
        temp = bomb_s[left_bound(bomb_s, v[0])]
    dist[v[1] - 1] = temp[1]
print(*dist)

for i, v in enumerate(vilages_s):
    # temp = left_bound(bomb_s, v[0]), right_bound(bomb_s, v[0])
    # print(left_bound(bomb_s, v[0]) + 1)
    if right_bound(bomb_s, v[0]) + 1 < len(bomb_s):
        temp = bomb_s[right_bound(bomb_s, v[0])]
    else:
        temp = bomb_s[right_bound(bomb_s, v[0])]
    dist_r[v[1] - 1] = temp[1]
print(*dist_r)

for i, v in enumerate(vilages_s):
    if v[0] - left_bound(bomb_s, v[0]) < right_bound(bomb_s, v[0]) - v[0]:
        temp = bomb_s[left_bound(bomb_s, v[0])]
    else:
        temp = bomb_s[right_bound(bomb_s, v[0])]
    dist_n[v[1] - 1] = temp[1]
print(*dist_n)
