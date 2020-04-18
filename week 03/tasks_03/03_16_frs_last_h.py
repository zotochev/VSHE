s = str(input())

s_back = s[::-1]
s_last = len(s) - (s_back.find('h'))
s_frs = s.find('h')

print(s[0:s.find('h')], s[s_last:len(s)], sep='')
