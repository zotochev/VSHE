file = 'input.txt'
# file = '06_16_input.txt'
fin = open(file, 'r', encoding='utf8')

marks_9 = []
marks_10 = []
marks_11 = []

for line in fin:
    temp = line.split()
    if temp[-2] == '9':
        marks_9.append(int(temp[-1]))
    elif temp[-2] == '10':
        marks_10.append(int(temp[-1]))
    else:
        marks_11.append(int(temp[-1]))

marks_9.sort()
marks_10.sort()
marks_11.sort()


def my_pop(my_list):
    temp = my_list[-1]
    while my_list[-1] == temp:
        del my_list[-1]


# print(marks_9, marks_10, marks_11)
my_pop(marks_9)
my_pop(marks_10)
my_pop(marks_11)
# print(marks_9, marks_10, marks_11)
print(marks_9[-1], marks_10[-1], marks_11[-1])
