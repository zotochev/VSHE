n = int(input())
x = float(input())
a_n = float(input())
count = 0

a_n_1 = 0

while count < n:
    count += 1
    a_n_1 = float(input())
    a_n = a_n * x + a_n_1

print(a_n)
