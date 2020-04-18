a = int(input())
b = int(input())
c = int(input())
# a = 1
# b = 2
# c = 3

d = 0
if a == b or b == c or a == c:
    d = 2
if a == b == c:
    d = 3
print(d)
