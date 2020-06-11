# file = '07_06_input.txt'
file = 'input.txt'

fin = open(file, 'r', encoding='utf8')
lst = []

for line in fin:
    # temp = line.readline()
    temp = line.strip()
    lst.extend(line.split())
print(len(set(lst)))
