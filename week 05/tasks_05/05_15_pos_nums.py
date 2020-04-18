s = list(map(int, input().split()))
count = 0
for num in s:
    if num > 0:
        count += 1
print(count)
