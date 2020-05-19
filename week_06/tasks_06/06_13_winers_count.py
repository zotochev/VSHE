fin = open('input.txt', 'r', encoding='utf8')

num = int(input())
contesters = []
max_mark = [0] * 3
max_mark_count = [0] * 3

for i in range(num):
    i = input().split()
    contesters.append(i)


for line in contesters:
    temp = line
    ssalc = temp[2]
    if ssalc == '9':
        ssalc = 0
    elif ssalc == '10':
        ssalc = 1
    else:
        ssalc = 2
    mark = int(temp[3])
    if max_mark[ssalc] <= mark:
        if max_mark[ssalc] != mark:
            max_mark_count[ssalc] = 0
        max_mark[ssalc] = mark
        max_mark_count[ssalc] += 1

# print(*max_mark)
print(*max_mark_count)
