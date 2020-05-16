s = list(map(int, input().split()))

min_1 = s.index(min(s))
max_1 = s.index(max(s))

s_min = s.copy()
s_max = s.copy()

# убираем наибольшее и наименьшее значения из списка
s_min.pop(min_1)
s_max.pop(max_1)

min_2 = min(s_min)
max_2 = max(s_max)

# в сокращённом списке найти второе по величине число
# возвращает индексы
min_2_i = s_min.index(min(s_min))
max_2_i = s_max.index(max(s_max))

# ищем третий множитель
s_min_3 = s_min.copy()
s_max_3 = s_max.copy()

# убираем наибольшее и наименьшее значения из списка
s_min_3.pop(min_2_i)
s_max_3.pop(max_2_i)

# ищем третий наибольший множитель
n_min_3 = min(s_min_3)
n_max_3 = max(s_max_3)


num1 = s[max_1] * s[min_1] * s_min[min_2_i]
num2 = s[max_1] * s_max[max_2_i] * n_max_3

if num1 > num2:
    print(s[max_1], s[min_1], s_min[min_2_i])
else:
    print(n_max_3, s_max[max_2_i], s[max_1])
