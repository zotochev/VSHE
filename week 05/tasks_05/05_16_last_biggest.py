s = list(map(int, input().split()))
big = [0, 0]

for idx, num in enumerate(s):
    if num >= big[0]:
        big[0], big[1] = num, idx
print(*big)
