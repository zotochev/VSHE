fin = open('input.txt', 'r', encoding='utf8')
x = []
a = 'a'

while len(a) > 0:
    a = fin.readline()
    x.append(a.strip())


print(x)
