s = list(map(int, input().split()))
sma = 0
count = 0

for i in s:
    if i > 0 and i:
        if count == 0:
            sma = i
        elif i < sma:
            sma = i
        # else:
        #     print('error')
        count += 1
print(sma)
