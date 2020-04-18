import math


def pre(n):
    return int(n ** (1 / 2)) ** 2


def back_line(n):
    if n == 0:
        return str('')
    else:
        return str(int(math.sqrt(pre(n)))) + ' ' + back_line(n - pre(n))


n = 48
print((back_line(n)))
a = back_line(n)
print(a.split(' '))
a = a.split(' ')

a1 = int(a[0])
a2 = int(a[1])
a3 = int(a[2])
a4 = int(a[3])

s = (a1 ** 2) + (a2 ** 2) + (a3 ** 2) + (a4 ** 2)

print(n, s, n == s)
