def power(a, n):
    p = 1
    if n > 0:
        while n != 0:
            n -= 1
            p *= a
    elif n < 0:
        while n != 0:
            n += 1
            p *= 1 / a
    else:
        p = 1
    return p


a, n = float(input()), int(input())
print(power(a, n))
