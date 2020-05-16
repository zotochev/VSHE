s = list(map(int, input().split()))
min = s.index(min(s))
max = s.index(max(s))
s[min], s[max] = s[max], s[min]
print(*s)
