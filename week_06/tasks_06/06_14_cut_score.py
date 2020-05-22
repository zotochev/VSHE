def cut_score(file):
    fin = open(file, 'r', encoding='utf8')
    k = int(fin.readline())
    scores = []

    for line in fin:
        temp = line.split()
        if int(temp[-1]) >= 40 and int(temp[-2]) >= 40 and int(temp[-3]) >= 40:
            scores.append(sum(map(int, temp[-3:])))
    scores.sort(key=lambda x: -x)

    scores_count = []
    prev_num = 0
    for num in range(len(scores)):
        num = scores[num]
        if num != prev_num:
            scores_count.append(scores.count(num))
        prev_num = num

    index_score = 0

    count = 0
    while len(scores_count) > count and k > index_score:
        index_score += scores_count[count]
        count += 1
    else:
        count -= 1
        if index_score > k:
            index_score -= scores_count[count]

    index_score -= 1
    # print(k, scores, scores_count, scores[index_score], sep='\n')

    def print_score(x):
        fout = open('output.txt', 'w', encoding='utf8')
        print(x, file=fout)
        fout.close()

    if (len(scores) != 0 and len(scores) <= k) or k == 0:
        '''Если будут зачислены все абитуриенты,
        не имеющие неудовлетворительных оценок,
        программа должна вывести число 0.'''
        print_score(0)
    elif len(scores) == 0 or scores_count[0] > k:
        '''Если количество имеющих равный максимальный балл
        абитуриентов больше чем K,
        программа должна вывести число 1.'''
        print_score(1)
    else:
        print_score(scores[index_score])


# files = 'input.txt'
# # # files = '06_14_input.txt'
# cut_score(files)

test_files = [
    ('06_14_input.txt', 1),
    ('06_14_input_test_1.txt', 200),
    ('06_14_input_test_2.txt', 0),
    ('06_14_input_test_3.txt', 1),
    ('06_14_input_test_4.txt', 0),
    ('06_14_input_test_5.txt', 0),
    ('06_14_input_test_6.txt', 0),
    ('06_14_input_test_7.txt', 0),
    ('06_14_input_test_8.txt', 200),
    ('06_14_input_test_9.txt', 210),
    ('06_14_input_test_10.txt', 0),
    ('06_14_input_test_11.txt', 210),
    ('06_14_input_test_12.txt', 1),
    ('06_14_input_test_13.txt', 1),
    ('06_14_input_test_14.txt', 148),
    ]


def test_cut_scores(test_list):
    for num, test in enumerate(test_list):
        cut_score(test[0])
        out_file = 'output.txt'
        fin = open(out_file, 'r', encoding='utf8')
        result = int(fin.readline())
        if result == test[1]:
            print('Test {0}: OK'.format(num))
        else:
            print(
                'Test {0}: NG. exp:{1}, get:{2}'.format(
                    num, test[1], result))


test_cut_scores(test_files)
