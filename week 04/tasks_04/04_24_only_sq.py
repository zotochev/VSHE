from math import sqrt


def only_sq():
    n = int(input())
    if n != 0:
        # if sqrt(n) % 1 == 0:
        if n % sqrt(n) == 0:
            only_sq()
            print(str(n), end=' ')
        else:
            only_sq()
            return ''
    else:
        return ''


only_sq()

# if only_sq() is not None:
#     only_sq()
# else:
#     print(0)
