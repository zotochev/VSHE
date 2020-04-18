l1 = int(input())
w1 = int(input())
h1 = int(input())
l2 = int(input())
w2 = int(input())
h2 = int(input())
lc = int(input())
wc = int(input())
hc = int(input())
# l1 = 4
# w1 = 1
# h1 = 2
#
# l2 = 3
# w2 = 3
# h2 = 2
#
# lc = 4
# wc = 3
# hc = 4

answer = 'TEST'

c1 = l1 + l2
c2 = l1 + w2
c3 = l2 + w1
c4 = w1 + w2
#
if c1 <= lc:
    if wc >= w1 and wc >= w2:
        answer = 'YES'
if c1 <= wc:
    if lc >= w1 and lc >= w2:
        answer = 'YES'

if c2 <= lc:
    if wc >= w1 and wc >= l2:
        answer = 'YES'
if c2 <= wc:
    if lc >= w1 and lc >= l2:
        answer = 'YES'

if c3 <= lc:
    if wc >= l1 and wc >= w2:
        answer = 'YES'
if c3 <= wc:
    if lc >= l1 and lc >= w2:
        answer = 'YES'

if c4 <= lc:
    if wc >= l1 and wc >= l2:
        answer = 'YES'
if c4 <= wc:
    if lc >= l1 and lc >= l2:
        answer = 'YES'

if answer != 'YES':
    if h1 + h2 <= hc:
        answer = 'YES'
    else:
        answer = 'NO'

if l1 > lc and l1 > wc or w1 > lc and w1 > wc or h1 > hc:
    answer = 'NO'
if l2 > lc and l2 > wc or w2 > lc and w2 > wc or h2 > hc:
    answer = 'NO'
print(answer)
