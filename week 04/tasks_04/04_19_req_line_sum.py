def line_sum():
    n = int(input())
    if n != 0:
        return n + line_sum()
    else:
        return 0


print(line_sum())
