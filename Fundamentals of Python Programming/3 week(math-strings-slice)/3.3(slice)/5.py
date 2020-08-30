"""
Дана строка. Найдите в этой строке второе вхождение буквы f и выведите индекс этого вхождения.
Если буква f в данной строке встречается только один раз, выведите число -1, а если не встречается ни разу,
выведите число -2.

При решении этой задачи нельзя использовать метод count.
"""

string = input()
if string.find('f') == -1:
    print(-2)
else:
    print(string.find('f', string.find('f') + 1))