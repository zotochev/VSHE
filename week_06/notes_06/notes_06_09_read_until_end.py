fin = open('text.txt', 'r', encoding='utf8')
a = 'a'
x = []
while len(a) > 0:
    a = fin.readline()
    x.append(a.strip())
    x.append('q')
print(x)
