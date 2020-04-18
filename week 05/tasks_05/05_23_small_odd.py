s = list(map(int, input().split()))
sma = 0
count = 0

for i in s:
    if i % 2 != 0:
        if count == 0:
            sma = i
        elif i < sma:
            sma = i
        count += 1
print(sma)
