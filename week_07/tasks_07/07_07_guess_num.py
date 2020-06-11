# file = '07_07_input.txt'
file = 'input.txt'

fin = open(file, 'r', encoding='utf8')
full_set = set()

prev = ''
num = int(fin.readline())

for i in range(1, num + 1):
    full_set.add(i)

for line in fin:
    if 'YES' in line:
        full_set &= set(map(int, prev.split()))
    elif 'NO' in line:
        full_set -= set(map(int, prev.split()))
    elif 'HELP' in line:
        print(*sorted(list(full_set)))
    else:
        prev = line
