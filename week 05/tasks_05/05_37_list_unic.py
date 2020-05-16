s = list(map(int, input().split()))
s_un = []

for x in s:
    if s.count(x) == 1:
        s_un.append(x)
print(*s_un)
