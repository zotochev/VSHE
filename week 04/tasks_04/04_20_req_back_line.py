def back_line():
    n = int(input())
    if n == 0:
        return print(n)
    else:
        back_line()
        return print(n)


back_line()
