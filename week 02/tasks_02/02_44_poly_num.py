n = int(input())
count_poly = 0
while n > 0:
    count = 0
    count_pow = 1
    n1 = 0
    n2 = 0
    n11 = 0
    n22 = 0
    n33 = 0
    n_bac = 0
    x = 0

    x = n % 10

    while n != x:
        count += 1
        x = n % 10 ** count
        # print(x, count)
    count2 = count
    while count >= count_pow:
        n2 += n1
        n1 = n % 10 ** (count_pow)
        n22 = n1 // 10 ** (count_pow - 1)
        count_pow += 1
        n1 = n1 - n2
        n11 = n1 * 10 ** (count_pow)
        n33 = n22 * 10 ** (count2 - 1)
        count2 -= 1
        n_bac += n33
        # print(n1, n2, n22, n33)
    if n % 10 == n:
        n_bac = n
    # print(n, n_bac)
    if n == n_bac:
        count_poly += 1
    n -= 1
print(count_poly)
