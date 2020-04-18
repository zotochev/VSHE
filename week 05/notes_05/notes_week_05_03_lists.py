# a = [1, (2, 3), 'a', [5, 6]]
# b = [1, 2, 3]
# # b = a[:]
# a[0] = 4
# print(a)
# print(b)


# def replace(flist):
#     flist[0] = 0


# a = [1, 2, 3]
# replace(a)
# print(a)



# def revirse(flist):
#     flist = flist[::-1]
#
#
# a = [1, 2, 3]
#
# revirse(a)
# print(a)


# a = list('abcde')
# a[0] = 'f'
# print(a)
# s = ''.join(a)
# print(s)


# word_split = input().split('a')
# print(word_split)


word_split = list(map(int, input().split()))
# print(' '.join(map(str, word_split)))
print(*word_split)
