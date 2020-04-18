s = list(map(int, input().split()))
count = 0

for idx, num in enumerate(s):
    if idx >= 1 and idx < len(s) - 1:
        if num > s[idx - 1] and num > s[idx + 1]:
            count += 1
print(count)

# 1 5 1 5 1
