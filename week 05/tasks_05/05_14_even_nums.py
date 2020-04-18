s = list(map(int, input().split(' ')))
nums = []
for num in s:
    if num % 2 == 0:
        nums.append(num)
# print(*nums)
print(' '.join(map(str, nums)))
