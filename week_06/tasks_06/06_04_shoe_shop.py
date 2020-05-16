foot_size = int(input())
shop_shoes_range = list(map(int, input().split()))


def how_many_shoes(foot_size, shop_shoes_range):
    '''
        Одну пару обуви можно надеть на другую, если она хотя бы на три размера
        больше.
        Максимальное количество пар обуви, которое сможет надеть покупатель.
    '''
    count = 0
    shoe = 0
    shop_shoes_range.sort()
    for n in shop_shoes_range:
        if count != 0:
            if n >= shoe + 3:
                count += 1
                shoe = n

        else:
            if n >= foot_size:
                count += 1
                shoe = n
    return count


def hms_test_algorithm():
    def hms_test_algorithm_1():
        foot_size = 60
        shop_shoes_range = [60, 63]
        if how_many_shoes(foot_size, shop_shoes_range) == 2:
            print("test 1: OK")
        else:
            print(
                "test 1: Fail: ",
                how_many_shoes(foot_size, shop_shoes_range)
                )

    def hms_test_algorithm_2():
        foot_size = 26
        shop_shoes_range = [30, 35, 40, 41, 42]
        if how_many_shoes(foot_size, shop_shoes_range) == 3:
            print("test 2: OK")
        else:
            print(
                "test 2: Fail: ",
                how_many_shoes(foot_size, shop_shoes_range)
                )

    def hms_test_algorithm_3():
        foot_size = 43
        shop_shoes_range = [43]
        if how_many_shoes(foot_size, shop_shoes_range) == 1:
            print("test 3: OK")
        else:
            print(
                "test 3: Fail: ",
                how_many_shoes(foot_size, shop_shoes_range)
                )

    def hms_test_algorithm_4():
        foot_size = 50
        shop_shoes_range = [48, 49]
        if how_many_shoes(foot_size, shop_shoes_range) == 0:
            print("test 4: OK")
        else:
            print(
                "test 4: Fail: ",
                how_many_shoes(foot_size, shop_shoes_range)
                )

    def hms_test_algorithm_5():
        foot_size = 50
        shop_shoes_range = [50, 50, 50]
        if how_many_shoes(foot_size, shop_shoes_range) == 1:
            print("test 5: OK")
        else:
            print(
                "test 5: Fail: ",
                how_many_shoes(foot_size, shop_shoes_range)
                )

    hms_test_algorithm_1()
    hms_test_algorithm_2()
    hms_test_algorithm_3()
    hms_test_algorithm_4()
    hms_test_algorithm_5()


# hms_test_algorithm()
print(how_many_shoes(foot_size, shop_shoes_range))
