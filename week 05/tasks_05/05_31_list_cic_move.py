s = list(map(int, input().split()))
s.insert(0, s.pop())
print(*s)
