file = 'input.txt'
# file = '07_09_input.txt'
fin = open(file, 'r', encoding='utf8')
n = int(fin.readline())

all_know = set()
all_langs = set()
count = 0

for lang in fin:
    if lang.strip().isdigit():
        student = set()
        for i in range(int(lang)):
            temp = fin.readline().strip()
            student.add(temp)
            all_langs.add(temp)
            if count == 0:
                all_know.add(temp)
        count += 1
        all_know &= student
print(len(all_know), *all_know, len(all_langs), *all_langs, sep='\n')
