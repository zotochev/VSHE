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
        for idx, i in enumerate(s_list):
            # if i < sl:
            if idx < sl - 1:
                if i > s_list[idx + 1]:
                    count2 += 1
                    s_list[idx], s_list[idx + 1] = s_list[idx + 1], s_list[idx]

print(*s_list)
# print(count1, count2)
