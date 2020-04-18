def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)


a, n = float(input()), int(input())

# a = 2
# n = 3
print(power(a, n))
