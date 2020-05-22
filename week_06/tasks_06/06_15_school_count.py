file = 'input.txt'
# file = '06_15_input.txt'
fin = open(file, 'r', encoding='utf8')

school_list = []
for school in fin:
    temp = school.split()
    school_list.append(temp[-2])

school_list.sort()
# print(school_list)
school_count = []
prev_num = 0

for num in range(len(school_list)):
    num = school_list[num]
    if num != prev_num:
        school_count.append((num, school_list.count(num)))
    prev_num = num

school_count.sort(key=lambda x: -x[1])
school_count_short = []
m = school_count[0][1]
for num in school_count:
    if num[1] == m:
        school_count_short.append(int(num[0]))

school_count_short.sort()
print(*school_count_short)
