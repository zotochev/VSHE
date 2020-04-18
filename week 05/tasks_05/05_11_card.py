n = int(input())
d = 0
for i in range(1, n):
    n += i
    d += int(input())
print(n - d)
