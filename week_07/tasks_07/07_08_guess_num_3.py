# file = '07_08_input_2.txt'
file = 'input.txt'

fin = open(file, 'r', encoding='utf8')
num = int(fin.readline())

full_set = set(map(str, [*range(1, num + 1)]))

guess_list = []

for line in fin:
    if 'HELP' not in line:
        yes = full_set.intersection(set(line.split()))
    else:
        break

    if len(yes) * 2 > len(full_set):
        print('YES')
        full_set = yes
    else:
        print('NO')
        no = full_set.difference(set(line.split()))
        full_set = no

print(*sorted(map(int, full_set)))
