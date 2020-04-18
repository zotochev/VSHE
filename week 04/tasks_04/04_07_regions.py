x = float(input())
y = float(input())


def un_line1(x, y):
    return -x >= y


def un_line2(x, y):
    return 2 * x + 2 >= y


def ab_line1(x, y):
    return -x <= y


def ab_line2(x, y):
    return 2 * x + 2 <= y


def in_circ_ab(x, y):
    return 4 >= ((x + 1) ** 2) + ((y - 1) ** 2)


def in_circ_bot(x, y):
    return 4 > ((x + 1) ** 2) + ((y - 1) ** 2)


def tr1(x, y):
    if un_line1(x, y) and un_line2(x, y):
        if not in_circ_bot(x, y):
            return True
        else:
            return False
    else:
        return False


def tr2(x, y):
    if ab_line1(x, y) and ab_line2(x, y) and in_circ_ab(x, y):
        return True
    else:
        return False


if tr1(x, y) or tr2(x, y):
    print('YES')
else:
    print('NO')
