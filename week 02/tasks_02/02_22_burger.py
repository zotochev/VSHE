k = int(input())
m = int(input())
n = int(input())
# вместимость сковороды
# k = 1

# время для прожарки одной стороны
# m = 2

#  За какое наименьшее время удастся поджарить с обеих сторон n котлет?
# n = 5

# Сколькко минут?

pod = (n * 2) // k
if (n * 2) % k > 0:
    pod_ost = 1
else:
    pod_ost = 0

if k >= n:
    pod_tot = m * 2
else:
    pod_tot = (pod + pod_ost) * m
print(pod_tot)
