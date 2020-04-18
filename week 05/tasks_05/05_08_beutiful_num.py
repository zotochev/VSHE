for i in range(10, 100):
    n = tuple(str(i))
    if i == 2 * int(n[0]) * int(n[1]):
        print(i)
