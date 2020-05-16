s = list(map(int, input().split()))
users_data = []
users_data_small = 0
count = 0

for n in range(s[1]):
    user = int(input())
    users_data.append(user)

users_data.sort()

for n in users_data:
    users_data_small += n
    if users_data_small >= s[0]:
        break
    else:
        count += 1

print(count)
