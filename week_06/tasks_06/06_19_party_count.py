file = 'input.txt'
# file = '06_19_input.txt'
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


for index, vote in enumerate(votes_test):
    votes_test[index] = vote, parties[index]


def party_sort(part):
    return (-part[0], part[1])


votes_test.sort(key=party_sort)
for party in votes_test:
    print(party[1])
