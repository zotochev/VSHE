import math
x = float(input())
n_count = 0

x_sum = 0
x_sum_2 = 0

while x != 0:
    n_count += 1

    x_sum += x
    x_sum_2 += x ** 2
    x = float(input())

stack = x_sum_2 - ((x_sum ** 2) / n_count)
sigma = math.sqrt(stack / (n_count - 1))
print(sigma)
