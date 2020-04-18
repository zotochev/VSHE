a = int(input())
b = int(input())
aa = (a // b)
bb = (b // a)
cc = aa * bb
print(((aa ** bb) * a + (bb ** aa) * b) // (1 + cc))
