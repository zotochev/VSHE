s = str(input())
s_back = s[::-1]
s_last = len(s) - (s_back.find('f') + 1)
s_frs = s.find('f')
if s_frs != -1:
    if s_frs == s_last:
        print(s_frs)
    else:
        print(s.find('f'), s_last)
