n = int(input())
# n = 5
count = 1
le = 0

for x in range(1, n + 1):
    count *= x
    le += count
print(le)
