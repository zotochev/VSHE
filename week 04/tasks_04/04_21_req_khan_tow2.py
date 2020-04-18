# +1
def khan_tow(n):
    if n > 3:
        m = (n - 1) % 3 + 1
        # m = n % 3
    else:
        m = n
    if n == 1:
        print(n, m)
        # print(m)
    else:
        khan_tow(n - 1)
        print(n, m)
        # print(m)


khan_tow(9)
