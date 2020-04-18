now = int(input())
maxnum = now
while now != 0:
    now = int(input())
    if now == 0:
        break
    if now > maxnum:
        maxnum = now
print(maxnum)
