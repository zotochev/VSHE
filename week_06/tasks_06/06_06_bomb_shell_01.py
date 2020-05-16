# def left_bound(a, key):
#     left = -1
#     right = len(a)
#     while right - left > 1:
#         middle = (left + right) // 2
#         if a[middle] < key:
#             left = middle
#         else:
#             right = middle
#     return left
#
#
# def right_bound(a, key):
#     left = -1
#     right = len(a)
#     while right - left > 1:
#         middle = (left + right) // 2
#         if a[middle] <= key:
#             left = middle
#         else:
#             right = middle
#     return right
#
#
vilages_num = int(input())
vilages = list(map(int, input().split()))
vilages_s = []
bomb_num = int(input())
bomb = list(map(int, input().split()))
bomb_s = []
dist = [0] * vilages_num


for i, x in enumerate(vilages):
    temp = x, i
    vilages_s.append(temp)

for i, x in enumerate(bomb):
    temp = x, i + 1
    bomb_s.append(temp)

# print(vilages_s)
# print(bomb_s)


def key_sort(a):
    return a[0]


vilages_s.sort(key=key_sort)
# print(vilages_s)
bomb_s.sort(key=key_sort)
# print(bomb_s)

for vilage in vilages_s:
    for i, bomb in enumerate(bomb_s):
        if i == 0:
            dist[vilage[1]] = bomb[1]
            dist_len = abs(vilage[0] - bomb[0])
        else:
            if dist_len > abs(vilage[0] - bomb[0]):
                dist[vilage[1]] = bomb[1]
                dist_len = abs(vilage[0] - bomb[0])

print(*dist)
