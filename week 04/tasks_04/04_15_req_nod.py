def gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


a, b = int(input()), int(input())

# a = 137
# b = 193
print(gcd(a, b))
