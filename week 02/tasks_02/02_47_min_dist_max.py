n1 = int(input())
n2 = int(input())
n3 = int(input())
count = 0

# координаты максимумов
count_max = 0
count_max_prev = 0

# расстояния между максимумами
count_max_dist = 0
count_max_dist_prev = 0

while n3 != 0:
    # общий счётчик
    count += 1

    # условие для максимума
    if n1 < n2 and n3 < n2:
        # print('-> if check max: ', count)
        # если условие выполнилось тогда
        # записываем значение общего счетчика как координату максимума
        # и записываем предыдущее значение максимума
        count_max_prev = count_max
        count_max = count

        # условие для первого прохода (исключение единицы)
        if count_max_prev == 0:
            count_max_prev = count_max

        # высчитываем растояние между максимумами
        # count_max_dist_prev = count_max_dist
        count_max_dist = count_max - count_max_prev

        # перезаписываем расстояние между максимумами
        # если текущее меньше предыдущего
        if count_max_dist_prev == 0 or count_max_dist_prev > count_max_dist:
            count_max_dist_prev = count_max_dist
            # print('-> if check max rewrite: ', count_max_dist_prev)

    # перезаписываем значение переменных
    n1 = n2
    n2 = n3
    n3 = int(input())
    # print(n1, n2, n3)
    # print('-> ', count, count_max, count_max_prev)
    # print('-> ', count_max_dist, count_max_dist_prev)

if count_max_dist_prev > count_max_dist:
    # print('-> if check max rewrite after while')
    count_max_dist_prev = count_max_dist

# случай если только два максимума
# if count_max_dist_prev == 0:
#     count_max_dist_prev = count_max_dist

print(count_max_dist_prev)
# print('-> ', count, count_max, count_max_prev)
# print('-> ', count_max_dist, count_max_dist_prev)
