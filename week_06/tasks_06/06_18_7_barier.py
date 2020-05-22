file = 'input.txt'
# file = '06_18_input.txt'
fin = open(file, 'r', encoding='utf8')

fin.readline()

parties = []
temp = ''
while ':' not in temp:
    temp = fin.readline().strip()
    parties.append(temp)

del parties[-1]

votes = []

for line in fin:
    votes.append(line.strip())

votes_test = [0] * len(parties)

for index, party in enumerate(parties):
    votes_test[index] = votes.count(party)

votes_count = sum(votes_test)

for index, count in enumerate(votes_test):
    if count / votes_count >= .07:
        print(parties[index])
