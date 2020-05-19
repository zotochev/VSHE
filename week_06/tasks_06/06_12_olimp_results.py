def mark_sort(contester):
    contester[1]


num = int(input())
contesters = []

for i in range(num):
    i = input().split()
    contesters.append(i)

contesters.sort(key=lambda x: -int(x[1]))

for con in contesters:
    print(con[0])
