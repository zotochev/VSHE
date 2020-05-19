fin = open('input.txt', 'r', encoding='utf8')
max_mark = [0] * 3

for line in fin:
    temp = list(line.split())
    ssalc = temp[2]
    if ssalc == '9':
        ssalc = 0
    elif ssalc == '10':
        ssalc = 1
    else:
        ssalc = 2
    mark = int(temp[3])
    if max_mark[ssalc] < mark:
        max_mark[ssalc] = mark

print(*max_mark)
