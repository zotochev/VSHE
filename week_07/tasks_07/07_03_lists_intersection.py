s1 = list(set(list(
    map(int, input().split()))) & set(list(map(int, input().split()))))

print(*sorted(s1))
