s = list(map(int, input().split()))
big = s[0]
for idx, num in enumerate(s):
    if idx != 0:
        if num > big:
            big = num
print(big, s.index(big))
