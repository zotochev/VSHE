# l1 = int(input())
# w1 = int(input())
# h1 = int(input())
#
# l2 = int(input())
# w2 = int(input())
# h2 = int(input())
#
# lc = int(input())
# wc = int(input())
# hc = int(input())

l1 = 3
w1 = 2
h1 = 2

l2 = 3
w2 = 1
h2 = 2

lc = 5
wc = 2
hc = 3

answer = 'TEST'

c1 = l1 + l2
c2 = l1 + w2
c3 = l2 + w1
print(lc, wc)
print(c1, c2, c3)

# if lc <= (c1 or c2 or c3) or wc <= (c1 or c2 or c3):
#     answer = 'YES1'
if c1 <= lc:
    print('test1')
    if wc <= (w1 and w2):
        answer = 'YES11'
    else:
        if c1 <= wc:
            if lc <= (w1 and w2):
                answer = 'YES12'
if c2 <= lc:
    print('test2')
    if wc <= (w1 and w2):
        answer = 'YES21'
    else:
        if c2 <= wc:
            if lc <= (w1 and w2):
                answer = 'YES22'
if c3 <= lc:
    print('test3')
    if wc <= (w1 and w2):
        answer = 'YES31'
    else:
        if c3 <= wc:
            if lc <= (w1 and w2):
                answer = 'YES32'
if answer != 'YES':
    if h1 + h2 <= hc:
        answer = 'YES4H'
    else:
        answer = 'NO'

if l1 > (lc or wc) or w1 > (lc or wc) or h1 > hc:
    answer = 'NO'
if l2 > (lc or wc) or w2 > (lc or wc) or h2 > hc:
    answer = 'NO'
print(answer)
