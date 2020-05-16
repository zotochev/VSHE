def key_sort(a):
    return a[0]


def cort(a, b):
    for i, n in enumerate(a):
        temp = n, i
        b.append(temp)
    # b.sort(key=key_sort)
    b.sort()
    return b


def civil_defence(villages, bomb_shell, n, m):
    villages_sort = []
    bomb_shell_sort = []

    villages_shell = [0] * n
    count = 1

    cort(villages, villages_sort)
    cort(bomb_shell, bomb_shell_sort)

    for vil in villages_sort:
        while count < m and (
            abs(vil[0] - bomb_shell_sort[count - 1][0]) > abs(
                vil[0] - bomb_shell_sort[count][0])):
            count += 1
            # print(count)
        villages_shell[vil[1]] = bomb_shell_sort[count - 1][1] + 1

    return villages_shell


def civil_defence_test():
    a = [1, 2, 6, 10]
    b = [7, 3]
    if civil_defence(a, b, len(a), len(b)) == [2, 2, 1, 1]:
        print('test1: OK')
    else:
        print('test1: NG')

    a = [1]
    b = [2]
    if civil_defence(a, b, len(a), len(b)) == [1]:
        print('test2: OK')
    else:
        print('test2: NG')

    a = [79, 64, 13, 8, 38, 29, 58, 20, 56, 17]
    b = [53, 19, 20, 85, 82, 39, 58, 46, 51, 69]
    if civil_defence(a, b, len(a), len(b)) == [5, 10, 2, 2, 6, 3, 7, 3, 7, 2]:
        print('test3: OK')
    else:
        print('test3: NG')

    a = [0, 1]
    b = [2, 3]
    if civil_defence(a, b, len(a), len(b)) == [1, 1]:
        print('test4: OK')
    else:
        print('test4: NG')

    a = [2, 3]
    b = [0, 1]
    if civil_defence(a, b, len(a), len(b)) == [2, 2]:
        print('test5: OK')
    else:
        print('test5: NG')

    a = [6810]
    b = [
        9462, 2762, 6699, 8881, 5323, 7801, 7980, 9781, 5354, 9423,
        1043, 5509, 9622, 9530, 6158, 740, 659, 5150, 7791, 2408,
        5496, 7786, 5833, 2209, 5235, 1737, 9847, 3431, 4083, 3797,
        4969, 9388, 5510, 6358, 9212, 2560, 4911, 9303, 4388, 7635,
        8051, 5386, 7176, 3526, 769, 9826, 3146, 8731, 6892, 8349,
        3170, 5722, 582, 3701, 2583, 6021, 7306, 956, 1193, 7011,
        7126, 3221, 4301, 2681, 691, 6418, 4742, 3095, 5763, 8679,
        4605, 2990, 4790, 6333, 9900, 2735, 4057, 9171, 3084, 6991,
        5244, 4095, 2409, 4614, 4365, 1554, 3183, 5015, 2614, 4042,
        2756, 9386, 8896, 6145, 5810, 3781, 2307, 9602, 8798, 4827]
    if civil_defence(a, b, len(a), len(b)) == [49]:
        print('test6: OK', civil_defence(a, b, len(a), len(b)))
    else:
        print('test6: NG', civil_defence(a, b, len(a), len(b)))


n = int(input())
villages = list(map(int, input().split()))
m = int(input())
bomb_shell = list(map(int, input().split()))

print(*civil_defence(villages, bomb_shell, n, m))
# civil_defence_test()
