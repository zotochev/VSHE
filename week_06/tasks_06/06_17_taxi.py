file = 'input.txt'
# file = '06_17_input.txt'
fin = open(file, 'r', encoding='utf8')

distance = list(map(int, fin.readline().split()))
tax = list(map(int, fin.readline().split()))
distance.sort(key=lambda x: -x)
tax.sort()

sum_money = 0
for num in range(len(tax)):
    sum_money += distance[num] * tax[num]

print(sum_money)
