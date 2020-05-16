vilages_num = int(input())
vilages = list(map(int, input().split()))

bomb_num = int(input())
bomb = list(map(int, input().split()))

vilages_s = []
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
count = 0

for vilage in vilages_s:
    print(*dist)
    print(count)
    if count < len(bomb_s) - 1:
        if vilage[0] <= (
            bomb_s[count][0] + (bomb_s[count + 1][0] - bomb_s[count][0])
                ):
            dist[vilage[1]] = bomb_s[count][1]
    else:
        dist[vilage[1]] = bomb_s[count][1]
    count += 1

print(*dist)
