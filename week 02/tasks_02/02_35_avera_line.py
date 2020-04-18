n = int(input())
count = 0
sum = 0
while n != 0:
    sum += n
    n = int(input())
    count += 1
print(sum / count)
