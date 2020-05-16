s = list(map(int, input().split()))
p = int(input())
i = 0
# count = 0

while i < len(s):
    if s[i] < p:
        i += 1
        break
    i += 1

if s[0] < p:
    i = 1
elif p <= s[-1]:
    i = len(s) + 1

print(i)
