s = str(input())

s_len = len(s)
# Сначала выведите третий символ этой строки.
print(s[2])
# Во второй строке выведите предпоследний символ этой строки.
print(s[-2])
# В третьей строке выведите первые пять символов этой строки.
print(s[0:5])
# В четвертой строке выведите всю строку, кроме последних двух символов.
print(s[0:s_len - 2])
# В пятой строке выведите все символы с четными индексами
# (считая, что индексация начинается с 0, поэтому
# символы выводятся начиная с первого).
print(s[::2])
# В шестой строке выведите все символы с нечетными индексами,
# то есть начиная со второго символа строки.
print(s[1::2])
# В седьмой строке выведите все символы в обратном порядке.
print(s[::-1])
# В восьмой строке выведите все символы строки через один
# в обратном порядке, начиная с последнего.
# s_back = s[::-1]
print(s[-1::-2])
# В девятой строке выведите длину данной строки.
print(s_len)
