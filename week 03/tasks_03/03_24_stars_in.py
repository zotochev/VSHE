s = str(input())

let = '*'
count = 0
s_m = ''
while len(s) - 1 > count:
    s_m += s[count] + let
    count += 1
print(s_m, s[len(s) - 1], sep='')
