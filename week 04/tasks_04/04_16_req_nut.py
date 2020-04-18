def gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def nut(a, b):
    return print(a // gcd(a, b), b // gcd(a, b))


a, b = int(input()), int(input())

nut(a, b)
