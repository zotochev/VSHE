s = list(map(int, input().split()))
sma = []

for i in s:
    if i > 0:
        sma.append(i)

sml = sma[0]

for num in sma:
    if num < sml:
        sml = num
print(sml)
