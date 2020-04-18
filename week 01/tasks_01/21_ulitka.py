# A > B ≥ 0
# h = int(input())
# a = int(input())
# b = int(input())
h = 15
a = 10
b = 1

aa = 0 ** (a // h)
hh = 0 ** (h // a)
c = hh ** aa
# print(aa, hh)

bb = 0 ** (b ** h)
hb = 0 ** (h ** b)
# print(bb, hb)

test = 0 ** (a - 1)

top = (h - b)
bot = (a - b)
# print(bb, test)
print(((top // (bot)) ** (aa + hh)) + (bb - test))
