x = int(input())
len = x
while x != 0:
    if x > len:
        len = x
    x = int(input())
print(len)
