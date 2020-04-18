n = int(input())
count = 1
fib_num = 0
fib_num_2 = 0
fib_num_1 = 1
while count < n:
    count += 1
    fib_num = fib_num_1 + fib_num_2
    fib_num_2 = fib_num_1
    fib_num_1 = fib_num
print(fib_num_1)
