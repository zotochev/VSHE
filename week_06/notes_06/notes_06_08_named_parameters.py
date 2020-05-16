def my_min(first, *others):
    now_min = first
    for now in others:
        if now < now_min:
            now_min = now
    return now_min


print(my_min(5, 2, 3, 4))
print(my_min(1))
