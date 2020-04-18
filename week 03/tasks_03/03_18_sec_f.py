s = str(input())
let = 'f'

cut = s[s.find(let) + 1:len(s)]

if s.find(let) == -1:
    print(-2)
elif s.find(let) != -1 and cut.find(let) == -1:
    print(-1)
else:
    print(s.find(let) + cut.find(let) + 1)
