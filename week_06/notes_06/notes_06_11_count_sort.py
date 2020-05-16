my_list = list(map(int, input().split()))

new_list = []
for i in range(len(my_list)):
    new_list.append((my_list[i], i))
new_list.sort()
print(new_list)
for now in new_list:
    print(now[1])
