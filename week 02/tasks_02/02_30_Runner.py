x = int(input())
y = int(input())
# x = 10
# y = 10
k = 0
len = 0
while x < y:
    x = x + len * .1
    len = x
    k = k + 1
    # print(x)
if k == 0:
    k = 1
print(k)
