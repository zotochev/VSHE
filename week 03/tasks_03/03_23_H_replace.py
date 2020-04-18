s = str(input())
# s = 'In the hole in the ground there lived a hobbit'
let = 'h'
s_l = s.find(let)
s_r = s.rfind(let)
s_cut = s[s_l + 1:s_r]

print(s[:s_l + 1], s_cut.replace(let, 'H'), s[s_r:], sep='')
