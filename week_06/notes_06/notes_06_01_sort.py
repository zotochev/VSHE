# a = [3, 1, 2]
# a.sort()
# print(a)

# a = [3, 1, 2]
# b = sorted(a)
# b = sorted('sgdfgdshnsd')
# b = sorted(a, reverse=True)
# print(a, b)

# print((1, 2) < (3, 4))  # True
# print((1, 10) < (3, 4))  # True
# print((1, 2) < (1, 'abc'))  # Error
# print((1, 2) < (2, 'abc'))  # True
# точно также можно сравнивать списки

p = [
    (175, 'Vasja'),
    (172, 'Mikhail'),
    (175, 'Alex')]
p.sort(reverse=True)
print(*p)
