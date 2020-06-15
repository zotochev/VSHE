# file = 'input.txt'
file = '07_11_input.txt'

fin = open(file, 'r', encoding='utf8')

data = list(map(int, fin.readline().split()))
riots = set()

weekend = set()
for num in range(7, data[0] + 1, 7):
    temp = int(num)
    weekend.add(temp - 1)
    weekend.add(temp)

for party in fin:
    party = list(map(int, party.split()))
    temp = set(range(party[0], data[0] + 1, party[1]))
    riots |= temp

riots -= weekend
print(len(riots))
