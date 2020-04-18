def reverse():
    n = int(input())
    if n != 0:
        reverse()
        print(n)


reverse()


# def rec():
#     n = int(input())
#     if n != 0:
#         if n % 2 == 0:
#             print(n)
#         rec()
#         if n % 2 != 0:
#             print(n)
#
#
# rec()
