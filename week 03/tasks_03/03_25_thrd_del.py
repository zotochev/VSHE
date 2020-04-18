s = str(input())
# s = 'Python' #yton
s_m = ''
count = 0
while len(s) > count:
    if count % 3 != 0:
        s_m += s[count]
    count += 1
print(s_m)
