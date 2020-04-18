s = list(map(int, input().split()))

len_s = len(s)

for i in range(len(s) - 1, -1, -1):
    s.append(s.pop(i))

print(*s)
# check
