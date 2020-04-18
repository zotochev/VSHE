p = int(input())
x = int(input())
y = int(input())
k = int(input())

count = 0
fd_full = x * 100 + y

while count < k:
    count += 1
    fd = fd_full * p // 100
    fd_full += fd

fd_rub = fd_full // 100
fd_kop = fd_full % 100

print(fd_rub, fd_kop)
