key_num = int(input())
key_dur = list(map(int, input().split()))
key_press_num = int(input())
key_press = list(map(int, input().split()))

press_list = [0] * key_num

for i in key_press:
    press_list[i - 1] += 1

# print(key_dur)
# print(press_list)
for index, key in enumerate(press_list):
    if key > key_dur[index]:
        print('YES')
    else:
        print('NO')
