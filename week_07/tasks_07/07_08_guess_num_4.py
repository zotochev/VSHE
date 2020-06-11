fin = open('input.txt', 'r', encoding='utf8')
n = int(fin.readline())
possible = set()

for i in range(1, n + 1):
    possible.add(i)
for line in fin:
    line = line.strip()
    if line == 'HELP':
        break
    else:
        temp = set(map(int, line.split()))
        if len(possible & temp) <= len(possible) / 2:
            print('NO')
            possible -= temp
        else:
            print('YES')
            possible &= temp

print(*sorted(possible))
