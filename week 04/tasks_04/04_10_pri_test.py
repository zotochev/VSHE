def MinDivisor(n):
    count = 2
    while n % count != 0:
        count += 1
        if count > n ** 0.5:
            return n
    return count


n = int(input())
# print(MinDivisor(n))
if MinDivisor(n) == n:
    print('YES')
else:
    print('NO')
