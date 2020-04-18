def khan_tow(n):
    # для чётных
    if n == 1:
        print(n, '+')
    else:
        khan_tow(n - 1)
        if n % 2 != 0:
            print(n, '+')
        else:
            print(n, '-')
        khan_tow(n - 1)
    # # для нечётных
    # if n == 1:
    #     print(n, '-')
    # else:
    #     khan_tow(n - 1)
    #     if n % 2 != 0:
    #         print(n, '-')
    #     else:
    #         print(n, '+')
    #     khan_tow(n - 1)

def kh_0(n):
    if n > 2:
        return n % 3, (n + 1) % 3
    else:
        return n, n + 1


def kh_1(n):
    if n > 2:
        return (n % 3) - 1, (n + 1) % 3
    else:
        return n - 1, n + 1


n = 2

khan_tow(n)
