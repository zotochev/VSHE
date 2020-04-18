s = str(input())

s_back = s[::-1]
s_last = len(s) - (s_back.find('h')) - 1
s_frs = s.find('h') + 1

print(s[0:s_frs], s[s_frs:s_last] * 2, s[s_last:len(s)],  sep='')
