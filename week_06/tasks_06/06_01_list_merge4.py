s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))
s = []

s1_count = 0
s2_count = 0

while True:
    if s1_count < len(s1) and s2_count < len(s2):
        if s1[s1_count] <= s2[s2_count]:
            s.append(s1[s1_count])
            s1_count += 1
        elif s1[s1_count] > s2[s2_count]:
            s.append(s2[s2_count])
            s2_count += 1
    else:
        if s1_count == len(s1):
            s.extend(s2[s2_count:])
            break
        else:
            s.extend(s1[s1_count:])
            break

print(*s)
