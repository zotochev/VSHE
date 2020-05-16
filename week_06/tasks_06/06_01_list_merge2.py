def to_sort(a, b, c):
    s_list = []
    if len(a) != 0 and len(b) != 0:
        if a[-1] > b[-1]:
            s_list.append(a.pop())
            to_sort(a, b, c)
        else:
            s_list.append(b.pop())
            to_sort(a, b, c)
    elif len(a) == 0:
        s_list.extend(b)
    else:
        s_list.extend(a)
    c += s_list


s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))
c = []

to_sort(s1, s2, c)
print(*c)
