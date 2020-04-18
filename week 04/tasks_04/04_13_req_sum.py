def sum(a, b):
    if b == 0:
        return a
    else:
        return sum(a + 1, b - 1)


a, b = int(input()), int(input())

# a = 6
# b = 3
print(sum(a, b))
