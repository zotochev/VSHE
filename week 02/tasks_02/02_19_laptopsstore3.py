a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
# a1 = 7
# b1 = 7
# c1 = 7
# a2 = 3
# b2 = 3
# c2 = 3

w1 = (a1 // a2) * (b1 // b2) * (c1 // c2)
w2 = (a1 // a2) * (b1 // c2) * (c1 // b2)
w3 = (a1 // b2) * (b1 // a2) * (c1 // c2)
w4 = (a1 // b2) * (b1 // c2) * (c1 // a2)
w5 = (a1 // c2) * (b1 // a2) * (c1 // b2)
w6 = (a1 // c2) * (b1 // b2) * (c1 // a2)

# print(w1, w2, w3, w4, w5, w6)

if w1 >= w2 and w1 >= w3:
    (g1, k11, k12) = (w1, w2, w3)
elif w2 >= w3 and w2 >= w1:
    (g1, k11, k12) = (w2, w1, w3)
else:
    (g1, k11, k12) = (w3, w1, w2)
# print(g1)

if w4 >= w5 and w4 >= w6:
    (g2, k21, k22) = (w4, w5, w6)
elif w5 >= w6 and w5 >= w4:
    (g2, k21, k22) = (w5, w4, w6)
else:
    (g2, k21, k22) = (w6, w4, w5)
# print(g2)

if g1 > g2:
    print(g1)
else:
    print(g2)
