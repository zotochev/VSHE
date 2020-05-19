fin = open('06_14_input.txt', 'r', encoding='utf8')
k = int(fin.readline())
print(k)
scores = []

for line in fin:
    print(line)
    temp = line.split()
    scores.append(temp[-3:])

print(scores)
