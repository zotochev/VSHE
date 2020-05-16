s = list(map(int, input().split()))
count = 0
s_com = []

for x in range(len(s)):
    s_com.append(0)
for idx, num in enumerate(s):
    if num != 0:
        s_com[count] = num
        count += 1

# if s.count(0) != 0:
#     while s.count(0) != 0:
#         s.pop(s.index(0))
#         count += 1
#     while count > 0:
#         s.append(0)
#         count -= 1


print(*s_com)
