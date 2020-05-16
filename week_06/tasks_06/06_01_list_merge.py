s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))

s_list = s1 + s2
sl = len(s1) + len(s2)
count1 = 0
count2 = 1
if s1[-1] > s2[0]:
    while count1 <= sl:
        count1 += 1
        if count2 == 0:
            break
        count2 = 0
        for i in range(sl - 1):
            if s_list[i] > s_list[i + 1]:
                count2 += 1
                s_list[i], s_list[i + 1] = s_list[i + 1], s_list[i]


print(*s_list)
# print(count1, count2)
