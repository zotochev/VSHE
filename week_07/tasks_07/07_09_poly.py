# file = 'input.txt'
file = '07_09_input.txt'
fin = open(file, 'r', encoding='utf8')
n = int(fin.readline())
poly_list = []
boy = 0

for num in range(n):
    poly_list.append(set())

count = 0
for lang in fin:
    lang = lang.strip()
    if lang.isdigit():
        boy = count
        count += 1
    else:
        poly_list[boy].add(lang)
print(poly_list)


for num in range(len(poly_list)):
    if num == 0:
        result_all = poly_list[num]
    else:
        result_all &= poly_list[num]
print(len(result_all), *result_all, sep='\n')

print(poly_list)
for num in range(len(poly_list)):
    if num == 0:
        result_list = poly_list[num]
        print(result_list)
    else:
        result_list |= poly_list[num]
        print(result_list)
print(len(result_list), *result_list, sep='\n')
