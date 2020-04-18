n = int(input())
count = 0
count_bac = 1
x = n % 10
n2 = 0
n22 = 0
while n != x:
    count += 1
    x = n % 10 ** count
    print(x, count)

n2 = n % (10 ** count_bac)
n22 = n2
n3 = n2 * 10 ** (count - 1)
print(n2, n3)
