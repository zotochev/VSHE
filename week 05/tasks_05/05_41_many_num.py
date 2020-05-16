s = list(map(int, input().split()))
s_count = []

for i in s:
    s_count.append(s.count(i))

print(s[s_count.index(max(s_count))])
