a = int(input())
count = 1
fib_num = 0
fib_num_2 = 0
fib_num_1 = 1
while fib_num < a:
    count += 1
    fib_num = fib_num_1 + fib_num_2
    fib_num_2 = fib_num_1
    fib_num_1 = fib_num
if fib_num_1 != a:
    print(-1)
else:
    print(count)
