s = list(map(int, input().split()))
num = s[0]
count = 1

for i in s:
    if i != num:
        num = i
        count += 1
print(count)
