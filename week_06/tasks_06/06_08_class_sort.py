fin = open('input.txt', 'r', encoding='utf8')
a = 'a'
mark_list = []

while len(a) > 0:
    a = fin.readline().strip()
    if a != '':
        mark_list.append(a.split())

mark_list.sort(key=lambda x: x[0])
# mark_list.pop()

for name in mark_list:
    print(name[0], name[1], name[3])
