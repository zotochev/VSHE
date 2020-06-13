file = 'input.txt'
# file = '07_10_input.txt'
fin = open(file, 'r', encoding='utf8')

inp = list(map(int, fin.readline().split()))

bus1 = [inp[0], inp[1]]
bus2 = [inp[2], inp[3]]

bus1.sort()
bus2.sort()

bus1 = set(range(bus1[0], bus1[1] + 1))
bus2 = set(range(bus2[0], bus2[1] + 1))
change = bus1 & bus2
print(len(change))
