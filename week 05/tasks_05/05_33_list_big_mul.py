s = list(map(int, input().split()))

min_1 = s.index(min(s))
max_1 = s.index(max(s))

s_min = s.copy()
s_max = s.copy()

s_min.pop(min_1)
s_max.pop(max_1)

min_2 = min(s_min)
max_2 = max(s_max)

num1 = s[min_1] * min_2
num2 = s[max_1] * max_2
if num1 > num2:
    print(s[min_1], min_2)
else:
    print(max_2, s[max_1])
