s = list(map(int, input().split()))
count = 0
k = []
keg = []

while count < s[1]:
    count += 1
    k.append(list(map(int, input().split())))

for i in range(s[0]):
    keg.append('I')

for i in range(0, s[1]):
    for j in range(k[i][0], k[i][1] + 1):
        keg[j - 1] = '.'
print(*keg, sep='')
