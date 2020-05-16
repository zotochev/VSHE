a = list(map(int, input().split()))
# for i in range(len(a)): # не работает

# работает, но медленно
# i = 0
# while i < len(a):
#     if a[i] % 2 != 0:
#         a.pop(i)
#     else:
#         i += 1
# print(*a)

# работает, но требует много памяти
b = []
for now in a:
    if now % 2 == 0:
        b.append(now)
print(*b)
