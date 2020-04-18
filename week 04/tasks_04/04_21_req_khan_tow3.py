# +2
def khan_tow(n):
    if n >= 1:
        m = ((n * 3) % 2) * 2
        # m = n % 3
    else:
        m = 0
    if n == 1:
        print(n, m)
        # print(m)
    else:
        khan_tow(n - 1)

        print(n, m)
        # print(m)


khan_tow(15)
