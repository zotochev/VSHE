my_list = list(map(int, input().split()))

grades = [0] * 11  # индекс задаёт оценку, а значение количество оценок

for now in my_list:
    grades[now] += 1

print(grades)

for grade in range(len(grades)):
    # print(grade)
    for i in range(grades[grade]):
        print(grade, end=' ')

    # print((str(grade) + ' ') * grades[grade], end=' ')
