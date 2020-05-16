s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))
s = []

s1_count = 0
s2_count = 0

while True:
    if len(s1) > s1_count and len(s2) > s2_count:
        if s1[s1_count] < s2[s2_count]:
            s1_count += 1
        elif s1[s1_count] > s2[s2_count]:
            s2_count += 1
        elif s1[s1_count] == s2[s2_count]:
            s.append(s1[s1_count])
            s1_count += 1
            s2_count += 1
    else:
        break
print(*s)
