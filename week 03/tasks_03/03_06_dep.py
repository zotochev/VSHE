p = int(input())
x = int(input())
y = int(input())


# proc = 10 ** (int(len(str(p))) - 1)
# fd_test = (x * 100 + y) * proc + (x * 100 + y) * p
fd = (x * 100 + y) + (x * 100 + y) * p // 100

fd_rub = fd // 100
fd_kop = int(fd % 100)

# print(fd_rub, ' ', fd_kop // 10, fd_kop % 10, sep='')
print(fd_rub, fd_kop)
