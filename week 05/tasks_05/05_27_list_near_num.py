k = int(input())
list = list(map(int, input().split()))
x = int(input())
count = list[0]

for i in list:
    if abs(x - i) < abs(x - count):
        count = i
    if i == x:
        count = i
        break
    # print(i, count)
print(count)
