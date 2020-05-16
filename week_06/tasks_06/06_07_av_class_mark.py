fin = open('input.txt', 'r', encoding='utf8')
av_marks = [[0, 0], [0, 0], [0, 0]]

a = list(fin.readlines())
for i, num in enumerate(a):
    a[i] = num.split()

for i in a:
    if int(i[2]) == 9:
        av_marks[0][0] = av_marks[0][0] + int(i[3])
        av_marks[0][1] += 1
    elif int(i[2]) == 10:
        av_marks[1][0] = av_marks[1][0] + int(i[3])
        av_marks[1][1] += 1
    else:
        av_marks[2][0] = av_marks[2][0] + int(i[3])
        av_marks[2][1] += 1
# print(a)

# print(av_marks)
for index, num in enumerate(av_marks):
    av_marks[index] = num[0] / num[1]
# print(list(map(lambda av_marks: )))
print(*av_marks)
