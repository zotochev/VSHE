s = []
s_st = []
s_line = []
check = True

for i in range(8):
    i = list(map(int, input().split()))
    s.append(i)
    if s_st.count(i[0]) == 0:
        s_st.append(i[0])
    else:
        check = False
    if s_line.count(i[1]) == 0:
        s_line.append(i[1])
    else:
        check = False

if check:
    for i in s:
        a = i[0] + i[1]  # x + y
        b = i[0] - i[1]  # x - y
        for j in s:
            if j[0] != i[0] and j[1] != i[1]:
                if b == j[0] - j[1] or a == j[0] + j[1]:
                    check = False

if check:
    print('NO')
else:
    print('YES')
