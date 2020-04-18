s = list(map(int, input().split()))
big = []
for idx, num in enumerate(s):
    if idx != 0:
        if s[idx - 1] < num:
            big.append(num)
print(' '.join(map(str, big)))
