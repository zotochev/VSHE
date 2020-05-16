class Man:
    height = 0
    name = ''


p = []
n = int(input())
for i in range(n):
    h, n = input().split()
    h = int(h)
    man = Man()
    man.height = h
    man.name = n
    p.append(man)


def make_tuple(man):
    return (man.height, man.name)


p.sort(key=make_tuple)
for now in p:
    print(now.height, now.name)
