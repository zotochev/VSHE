n = float(input())
m = 1
u = 0


def summ(x):
    return (1 / m ** 2)


while m <= n:
    u += summ(m)
    m += 1
print(u)
