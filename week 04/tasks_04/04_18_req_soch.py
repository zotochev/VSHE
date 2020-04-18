def soch(n, k):
    if n == k or k == 0:
        return 1
    elif k == 1:
        return n
    else:
        return soch(n - 1, k) + soch(n - 1, k - 1)


a, b = int(input()), int(input())
print(soch(a, b))
