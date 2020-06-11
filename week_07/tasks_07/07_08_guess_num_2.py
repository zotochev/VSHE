# file = '07_08_input_2.txt'
file = 'input.txt'

fin = open(file, 'r', encoding='utf8')
num = int(fin.readline())

full_set = set(map(str, [*range(1, num + 1)]))

# guess_list = []

for line in fin:
    if 'HELP' not in line:
        # yes = full_set & set(line.split())
        yes = full_set.intersection(set(line.split()))
        # no = full_set - set(line.split())
    else:
        break

    # if len(yes) > len(no):
    if len(yes) * 2 > len(full_set):
        print('YES')
        # guess_list.append('YES')
        full_set = yes
    # if len(yes) <= len(no) or len(line) == (num // 2):
    else:
        print('NO')
        # guess_list.append('NO')
        # no = full_set - set(line.split())
        no = full_set.difference(set(line.split()))
        full_set = no

# print(*guess_list, sep='\n')
print(*sorted(map(int, full_set)))
