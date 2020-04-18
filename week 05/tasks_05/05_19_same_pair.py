# def is_a_scending(a):
#     c = -1
#     stat = False
#     s = []
#     while stat is False and c < len(a) - 1:
#         c += 1
#         print(len(a) - 1)
#         print(c)
#         stat = (a[c + 1] > 0 and a[c] > 0) or (a[c + 1] < 0 and a[c] < 0)
#     if stat is True:
#         s.append(a[c])
#         s.append(a[c + 1])
#     print(*s)


def is_a_scending(a):
    for x, i in enumerate(a):
        if x != 0:
            ch = abs(a[x - 1] + i)
            if ch > abs(a[x - 1]) and ch > abs(i):
                print(a[x - 1], i)
                break


s = list(map(int, input().split()))
is_a_scending(s)
