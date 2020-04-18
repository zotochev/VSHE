def tow(n, a, c, b):
    if n != 0:
        tow(n - 1, a, b, c)
        print(n, a, c)
        tow(n - 1, b, c, a)


def tow_main(n):
    a = 1
    b = 2
    c = 3
    tow(n, a, c, b)


# n = 4
n = int(input())
tow_main(n)
